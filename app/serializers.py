from rest_framework import serializers

from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'first_name', 'last_name', 'email', 'role', 'department')


class UsersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'first_name', 'last_name', 'email', 'role', 'department', 'residental_address', 'age')