from django.db import models


class BlogPost(models.Model):

    def __str__(self):
        return self.title

    title = models.TextField()
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
