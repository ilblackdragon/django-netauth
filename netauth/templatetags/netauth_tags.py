from django.conf import settings

if 'coffin' in settings.INSTALLED_APPS:
    from coffin.template import Library
else:
    from django.template import Library

from netauth import settings as netauth_settings
from netauth.models import NetID

register = Library()

if 'coffin' in settings.INSTALLED_APPS:
    register.simple_tag = register.object

@register.filter
def option( value, name ):
    """ Return settings parameter from django or netauth settings.
    """
    return getattr(settings, name, '') or getattr(netauth_settings, name, '')

"""
    This tags from django-misc application - https://github.com/ilblackdragon/django-misc/tree/v0.0.1
    When django-misc app will be in PyPi, it will be removed from here
"""

@register.simple_tag
def get_providers(request):
    netids = NetID.objects.filter(user=request.user)
    providers = [netid.provider for netid in netids]
    return providers

@register.simple_tag
def insert_sign(providers, provider):
    if provider in providers:
        return """<div class="social-provider-sign social-provider-check"></div>"""
    else:
        return """<div class="social-provider-sign social-provider-uncheck"></div>"""

