from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe
from model_utils import Choices
from django.core.files.storage import default_storage

import django


class User(AbstractUser):
    photo = models.ImageField(_('Photo'), upload_to='userphotos/', null=True, blank=True)

    birthday = models.DateField(_('Birthday'), null=True, blank=True)
    location = models.CharField(_('Location'), max_length=255, null=True, blank=True)
    creation_time = models.DateTimeField(_('Creation Time'), default=django.utils.timezone.now)

    @property
    def longest_distance(self):
        try:
            driver_club = self.clubs.first()
            return driver_club.avg_dist
        except Exception as e:
            return None

    @property
    def photo_url(self):
        if not self.photo:
            return ''

        if default_storage.exists(self.photo.path):
            return '%s%s' % (settings.MEDIA_URL, self.photo)
        else:
            return ''

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150"/>' % self.photo_url)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
