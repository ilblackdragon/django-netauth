from django.conf import settings
from django.db import models

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class NetID(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL)
    identity = models.CharField(u'Net ID', max_length=255, unique=True)
    provider = models.CharField(u'Net authentication provider name', max_length=255)

    def __unicode__(self):
        return "%s -> %s" % (self.provider, self.identity)
