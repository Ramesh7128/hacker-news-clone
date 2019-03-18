from rest_framework import serializers
from top_articles.models import Story
from top_articles.models import User
from django.contrib.auth import authenticate


class StorySerializer(serializers.ModelSerializer):
    is_checked = serializers.SerializerMethodField('is_starred')

    def is_starred(self, instance):
        user = None
        try:
            request = self.context.get('request')
            if request and hasattr(request, 'user'):
                if not request.user.is_anonymous:
                    user = request.user
                    if Story.objects.filter(pk=instance.id, starred_user=user).exists():
                        return True
                    else:
                        return False
                else:
                    return None
            return None
        except Exception as error:
            print(error)
            return None

    class Meta:
        model = Story
        fields = '__all__'


class RegisterationSerializer(serializers.ModelSerializer):
    """
    Serializer to for registeration request and create a new user.
    """
    password = serializers.CharField(
        max_length=200,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=200, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        # use the create user method we wrote earlier to create a new_user.
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        # The 'validate' method is where we make sure that the user.
        # the validate method is where we make sure that the user is a valid user.

        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'Email field is required to log in')

        if password is None:
            raise serializers.ValidationError(
                'password field is required to log in')

        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError('User credentials not matching')

        if not user.is_active:
            raise serializers.ValidationError('User has been deactivated')

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):
    """
    Handles serialization and deserialization of user objects.
    """
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        # read_only_fields = ('token',)

    def update(self, instance, validated_data):
        """
        performs an update on User instance.
        """
        password = validated_data.pop('password', None)
        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance
