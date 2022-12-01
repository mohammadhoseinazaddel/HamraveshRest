from rest_framework import serializers
from container_apps.models import Author, ContainerApps
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ContainerAppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerApps
        fields = '__all__'
        depth = 1
