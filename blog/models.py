from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone

user = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        # the same as BlogPost.objects...can run .all, .filter, .get, etc.
        return self.filter(publish_date__lte=timezone.now())

    def search(self, query):
        lookup = (
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(slug__icontains=query) |
            Q(user__username__icontains=query)
        )
        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class BlogPost(models.Model):

    def __str__(self):
        return self.title
    # defaults to first user, when a user is deleted, the user gets set to NULL then defaults to user id 1.
    user = models.ForeignKey(user, default=1, null=True,
                             on_delete=models.SET_NULL)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    # Publish date can be manually set. auto is False. null and blank are okay as they could be published in the future
    publish_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    # These are handled automatically and thus will not appear in admin.
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        # - in front if you want the most recent of that field. omit - if you want oldest first
        ordering = ["-publish_date", "-updated", "-timestamp"]

    def get_absolute_url(self):
        return "/blog/{}".format(self.slug)

    def get_edit_url(self):
        return "{}/edit/".format(self.get_absolute_url())

    def get_delete_url(self):
        return "{}/delete/".format(self.get_absolute_url())
