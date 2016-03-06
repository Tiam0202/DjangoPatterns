from django.db import models
from django.utils.translation import ugettext_lazy as _


class Page(models.Model):
    """A simple HTML page
    """
    meta_title = models.CharField(_(u"Meta title"), blank=True, max_length=80)
    meta_keywords = models.TextField(_(u"Meta keywords"), blank=True)
    meta_description = models.TextField(_(u"Meta description"), blank=True)


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class Friendship(models.Model):
    from_friend = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='from_friends',
    )
    to_friend = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='friends',
    )
    length_in_months = models.IntegerField()
