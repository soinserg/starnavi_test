from django.contrib import admin

from .models import Post, PostVote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created', 'text')


@admin.register(PostVote)
class PostVoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'value', 'post')
