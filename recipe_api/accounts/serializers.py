from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authentication import authenticate
from rest_framework.exceptions import ValidationError

get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'password2', 'email', 'profile_picture', 'followers']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise ValueError({'password': 'Passwords must match'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')

        user = get_user_model().objects.create(username = validated_data['username'],
                                               email = validated_data['email'],
                                               profile_picture = validated_data.get('profile_picture', None)
                                               )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            raise ValidationError({'message':'Invalid username or password'})
        
        data['user'] = user
        return data
    
    def to_representation(self, instance):
        
        user = instance['user']
        token, _ = Token.objects.get_or_create(user=user)

        return{
            'message': 'Login successful',
            'Token': token.key
        }
       
class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'profile_picture', 'followers_count'] 

    def get_followers_count(self, obj):
        return obj.followers.count()

class AccountDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'profile_picture']

class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'profile_picture']


    

