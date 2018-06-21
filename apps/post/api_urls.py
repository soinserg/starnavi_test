from django.urls import path

from . import api_views
from .models import PostVote

app_name = 'api_post'
urlpatterns = [
    path('', api_views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', api_views.PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/like/', api_views.PostVoteCreate.as_view(value=PostVote.LIKE), name='post_like'),
    path('<int:pk>/dislike/', api_views.PostVoteCreate.as_view(value=PostVote.DISLIKE), name='post_dislike'),
]
