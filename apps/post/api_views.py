from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    CreateAPIView
)

from .models import Post, PostVote
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
    queryset = PostVote.objects.all()
    value = None

    def perform_create(self, serializer):
        author = self.request.user
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        try:
            PostVote.objects.get(author=author, post=post)
            raise ValidationError(_('Вы уже оценивали эту заметку'))
        except PostVote.DoesNotExist:
            serializer.save(
                value=self.value,
                author=author,
                post=post
            )
