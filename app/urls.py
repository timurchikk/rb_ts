from django.urls import path

from .views import UsersListView, UsersDetailView

urlpatterns = [
    path('users/', UsersListView.as_view(), name = 'Users list'),
    path('users/detail/<int:user_id>/', UsersDetailView.as_view(), name = 'user detail')
]
