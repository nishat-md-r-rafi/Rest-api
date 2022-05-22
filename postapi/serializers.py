from pprint import pprint
from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework.settings import api_settings
from .models import Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username')

# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     username = serializers.CharField(max_length=255)
#     email = serializers.EmailField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()

    class Meta:
        model = Post
        fields = ('post', 'created_at', 'updated_at', 'created_by')
        read_only_fields = ('created_by',)

    # def create(self, validated_data):
    #     pprint(validated_data)
    #     created_by = dict(validated_data['created_by'])

    #     created_user = User.objects.create_user(
    #         created_by['username'], created_by['email'],)
    #     return created_user
