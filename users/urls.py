from django.urls import path 
from .views import UserListsCreate, UserRetrieveUpdateDelete

urlpatterns = [
    path('users', UserListsCreate.as_view(), name="Create-User-List"),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name='user-Details')
]