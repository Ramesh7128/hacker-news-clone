from django.db import models
from .sentiment import calculate_sentiment
from django.contrib import admin

# Create your models here.
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
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        print("function called")
        self.sentiment_score = calculate_sentiment(self.title)
        super(Story, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "stories"


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)
    story = models.ManyToManyField('Story', related_name='categories',blank=True, null=True)


    
    

