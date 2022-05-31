from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    role = models.CharField(verbose_name='Role', max_length=100)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.role


class Department(models.Model):
    department = models.CharField(verbose_name='Deparment', max_length=50)

    class Meta:
        verbose_name = 'Depatrment'
        verbose_name_plural = 'Depatrments'

    def __str__(self):
        return self.department


class Address(models.Model):
    address = models.CharField(verbose_name='Address', max_length=50)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.address


class Users(models.Model):
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='First name', max_length=25)
    last_name = models.CharField(verbose_name='Last name', max_length=25)
    email = models.CharField(verbose_name='Email', max_length=50)
    role = models.ForeignKey(Role, verbose_name='Role', on_delete=models.PROTECT)
    department = models.ForeignKey(Department, verbose_name='Department', on_delete=models.PROTECT)
    residental_address = models.ForeignKey(Address, verbose_name='Address', on_delete=models.PROTECT)
    age = models.IntegerField(verbose_name='Age')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['first_name', 'last_name', 'email', 'role', 'department', 'residental_address']

    def __str__(self):
        return f'{self.email} - {self.first_name}'