from django.conf import settings
from django.db import models


class SearchQuery(models.Model):
    # https://stackoverflow.com/questions/24629705/django-using-get-user-model-vs-settings-auth-user-model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,
                             null=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)
