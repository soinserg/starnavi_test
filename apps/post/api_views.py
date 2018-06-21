from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    CreateAPIView
)

from .models import Post
from .serializers import PostSerializer, PostVoteSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostVoteCreate(CreateAPIView):
    serializer_class = PostVoteSerializer
    value = None

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        serializer.save(
            value=self.value,
            author=self.request.user,
            post=post
        )
