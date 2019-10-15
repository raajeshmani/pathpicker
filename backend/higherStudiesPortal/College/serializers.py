from rest_framework import serializers
from django.contrib.auth.models import User

from .models import (College,Course)

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields=['id','description','expenses','entrance_exam','courses','links']
        depth=1

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields=['id','name','description','c_type','offering_colleges']
        depth=1


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
