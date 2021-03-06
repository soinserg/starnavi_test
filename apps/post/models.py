from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    text = models.TextField(
        _('Текст')
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        verbose_name=_('Автор')
    )
    created = models.DateTimeField(
        _('Создан'),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('Заметка')
        verbose_name_plural = _('Заметки')
        ordering = ('-created',)

    def __str__(self):
        return self.text[:10]

    def like_count(self):
        return self.postvote_set.filter(value=PostVote.LIKE).count()

    def dislike_count(self):
        return self.postvote_set.filter(value=PostVote.DISLIKE).count()


class PostVote(models.Model):
    LIKE = 1
    DISLIKE = -1
    VALUE_CHOICES = (
        (LIKE, _('Нравится')),
        (DISLIKE, _('Не нравится')),
    )

    value = models.SmallIntegerField(
        _('Оценка'),
        choices=VALUE_CHOICES
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.SET_NULL,
        verbose_name=_('Автор'),
        null=True
    )
    post = models.ForeignKey(
        Post,
        models.CASCADE,
        verbose_name=_('Заметка')
    )

    class Meta:
        verbose_name = _('Оценка заметки')
        verbose_name_plural = _('Оценки заметок')
        unique_together = ('author', 'post')

    def __str__(self):
        return '%s %s %s' % (self.author, self.value, self.post)

    def post_info(self):
        return {
            'like_count': self.post.like_count(),
            'dislike_count': self.post.dislike_count()
        }
