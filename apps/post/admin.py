from django.contrib import admin

from .models import Post, PostVote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(PostVote)
class PostVoteAdmin(admin.ModelAdmin):
    pass
