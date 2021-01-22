from django.conf import settings
from django.db import models

user = settings.AUTH_USER_MODEL


class BlogPost(models.Model):

    def __str__(self):
        return self.title
    # defaults to first user, when a user is deleted, the user gets set to NULL then defaults to user id 1.
    user = models.ForeignKey(user, default=1, null=True,
                             on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return "/blog/{}".format(self.slug)

    def get_edit_url(self):
        return "{}/edit/".format(self.get_absolute_url())

    def get_delete_url(self):
        return "{}/delete/".format(self.get_absolute_url())
