from django.db import models
from .utils import string_generator, create_shortcode

class LessUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(LessUrlManager, self).all(*args, **kwargs).filter(active=True)
        return qs

    def refrash_shortcodes(self):
        qs = LessUrl.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {0}".format(new_codes)


class LessUrl(models.Model):

    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = LessUrlManager()

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(LessUrl, self).save(*args, **kwargs)

    def __unicode__(self):
        return set(self.url)

# Create your models here.
