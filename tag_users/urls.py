from django.urls import include, path
from .views import MatchedUsers, UserCreate, UserList, UserDetail, UserUpdate, UserDelete, MatchedUsers


urlpatterns = [
    path('create', UserCreate.as_view(), name='create-user'),
    path('', UserList.as_view()),
    path('<str:pk>', UserDetail.as_view(), name='retrieve-user'),
    path('update/<str:pk>', UserUpdate.as_view(), name='update-user'),
    path('delete/<str:pk>', UserDelete.as_view(), name='delete-user'),
    path('matches/<str:pk>', MatchedUsers.as_view(), name="matched-users")
]


