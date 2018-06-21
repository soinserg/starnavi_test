from rest_framework import serializers

from .models import Post, PostVote


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    like = serializers.IntegerField(source='like_count', read_only=True)
    dislike = serializers.IntegerField(source='dislike_count', read_only=True)

    class Meta:
        model = Post
        fields = ['pk', 'text', 'author', 'created',
                  'like', 'dislike']


class PostVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVote
        fields = ['post_info']
