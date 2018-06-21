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
    author = serializers.CharField(source='author.username', read_only=True)
    value = serializers.CharField(source='get_value_display', read_only=True)
    post = serializers.CharField(source='post.text', read_only=True)

    class Meta:
        model = PostVote
        fields = ['value', 'author', 'post']
