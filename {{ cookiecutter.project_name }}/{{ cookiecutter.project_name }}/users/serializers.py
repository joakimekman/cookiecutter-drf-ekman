from rest_framework import serializers, fields, validators
from .models import User


class UserSerializer(serializers.ModelSerializer):

    """Set the UniqueValidator of the `username` and `email` fields to `iexact`"""

    username = fields.CharField(
        max_length=150,
        validators=[validators.UniqueValidator(
            queryset=User.objects.all(),
            lookup='iexact',
            message='Username already exists.'
        )] 
    )
    email = fields.CharField(
        max_length=150,
        validators=[validators.UniqueValidator(
            queryset=User.objects.all(),
            lookup='iexact',
            message='Email already exists.'
        )]  
    )

    class Meta: 
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        

    def create(self, validated_data):
        """
        Override to change the create method that is used by default
        to create_user. Also converting the username and email input
        to lowercase.
        """

        user = User.objects.create_user(
            username=validated_data['username'].lower(),
            email=validated_data['email'].lower(),
            password=validated_data['password'],
            )
        return user


    