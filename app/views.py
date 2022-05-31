from django.shortcuts import render
from django.core.paginator import Paginator


from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from rest_framework import generics, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .models import Users
from .serializers import UsersSerializer, UsersDetailSerializer


class UsersListView(generics.ListAPIView):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email']


class UsersDetailView(generics.RetrieveAPIView):
    
    def get(self, *args, **kwargs):
        user = Users.objects.get(user__id=kwargs['user_id'])
        serilaizer = UsersDetailSerializer(user)
        return Response(serilaizer.data, status=status.HTTP_200_OK)