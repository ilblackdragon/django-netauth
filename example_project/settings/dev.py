# Settings for local debug (netauth.dev.me)
from settings.project import *

# Debug
DEBUG = True
TEMPLATE_DEBUG = True
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += ( 'debug_toolbar.middleware.DebugToolbarMiddleware', )
INSTALLED_APPS += ( 'debug_toolbar', )
DEBUG_TOOLBAR_CONFIG = dict( INTERCEPT_REDIRECTS = False)

# NETAUTH_SETTINGS
TWITTER_CONSUMER_KEY = "2NBsAXQ7rKheeEvjbg5wg"
TWITTER_CONSUMER_SECRET = "bhtnzprhzpsvOzcuLONKwEKrFtBxLpvqHJbbXjNYE"

FACEBOOK_APPLICATION_ID = "159934957395280"
FACEBOOK_APPLICATION_SECRET = "11fe68b045fb882e25fe22b192a0ac7e"

YANDEX_APPLICATION_ID = "02644cd63ed24c5692d553d0adccd597"

VKONTAKTE_APPLICATION_ID = "2224643"
VKONTAKTE_APPLICATION_SECRET = "FfkAZduBth0Sd1etoVT2"
