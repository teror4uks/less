from django.db import models


class LessUrl(models.Model):

    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return set(self.url)

# Create your models here.
