from django.db import models

from .utils import create_shortcode
from .validators import validate_url

from django.conf import settings
from django_hosts.resolvers import reverse

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class LessUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(LessUrlManager, self).all(*args, **kwargs).filter(active=True)
        return qs

    def refresh_shortcodes(self):
        qs = LessUrl.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {0}".format(new_codes)


class LessUrl(models.Model):

    url = models.CharField(max_length=220, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = LessUrlManager()

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if not 'http' in self.url:
            self.url = 'http://' + self.url

        super(LessUrl, self).save(*args, **kwargs)

    def __unicode__(self):
        return set(self.url)

    def get_short_url(self):
        url_path = reverse('scode', kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
        print(url_path)
        return url_path
