from rest_framework import serializers

from .models import Users, Role, Department, Address


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'role',)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'department',)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address',)


class UsersSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    department = DepartmentSerializer()
    class Meta:
        model = Users
        fields = ('user_id', 'first_name', 'last_name', 'email', 'role', 'department')


class UsersDetailSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    department = DepartmentSerializer()
    residental_address = AddressSerializer()
    class Meta:
        model = Users
        fields = ('user_id', 'first_name', 'last_name', 'email', 'role', 'department', 'residental_address', 'age')