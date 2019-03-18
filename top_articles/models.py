import jwt
from datetime import datetime, timedelta
from django.conf import settings

from django.db import models
from .sentiment import calculate_sentiment
from django.contrib import admin
from django.utils import timezone
from django.dispatch import receiver
from . import search
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager)
# Create your models here.


class UserManger(BaseUserManager):
    """
    custom create_user method for user model.
    """

    def create_user(self, username, email, password=None):
        """
        create and return a user object with username, email and password.
        """
        if username is None:
            raise TypeError('user must have a username')
        if email is None:
            raise TypeError('user must have a email')
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing fully featured User model with
    admin-compliant permissions.
    """
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManger()

    def __str__(self):
        """
        Returns a spring representation of this user
        """
        return self.email

    @property
    def token(self):
        """
        Allows us to get user token with user.token. @property decorator lets you do it.
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        This is required by django when handling emails.
        which is ideally first name and last name.
        But since we are not handling first name and last name
        we use username instead.
        """
        return self.username

    def get_short_name(self):
        """
        This method is used by django for handling emails.
        """
        return self.username

    def _generate_jwt_token(self):
        """
        Generates jwt that stores user ids and has an expiry date set to 50 days
        """
        dt = datetime.now() + timedelta(days=50)
        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')



class Story(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.TextField(blank=False, null=False)
    author = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    link = models.URLField()
    timestamp = models.IntegerField()
    top_order_no = models.IntegerField(null=True, unique=True)
    sentiment_score = models.FloatField(blank=True)
    new_order_no = models.IntegerField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    starred_user = models.ManyToManyField(User, related_name='starred_user')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.sentiment_score = calculate_sentiment(self.title)
        super(Story, self).save(*args, **kwargs)

    def indexing(self):
        obj = search.StoryIndex(
            meta={'id': self.id},
            id=self.id,
            title=self.title,
            author=self.author,
            score=self.score,
            link=self.link,
            timestamp=self.timestamp,
            created_at=self.created_at,
            sentiment_score=self.sentiment_score
        )
        obj.save(index='story-index')
        return obj.to_dict(include_meta=True)

    class Meta:
        verbose_name_plural = "stories"


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)
    story = models.ManyToManyField(
        'Story', related_name='categories', blank=True)
