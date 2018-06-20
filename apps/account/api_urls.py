from django.urls import path

from . import api_views

app_name = 'api_account'
urlpatterns = [
    path('', api_views.UserList.as_view(), name='user_list'),
    path('<int:pk>/', api_views.UserDetail.as_view(), name='user_detail'),
]
