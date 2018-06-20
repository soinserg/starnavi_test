from django.urls import path

from . import api_views

app_name = 'api_post'
urlpatterns = [
    path('', api_views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', api_views.PostDetail.as_view(), name='post_detail'),
]
