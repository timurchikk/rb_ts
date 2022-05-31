from django.shortcuts import render
from django.core.paginator import Paginator


from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

from .models import Users
from .serializers import UsersSerializer


class UsersListView(generics.ListAPIView):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email']
