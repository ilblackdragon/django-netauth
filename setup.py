import os

from setuptools import setup, find_packages

from netauth import VERSION, PROJECT, LICENSE


MODULE_NAME = 'netauth'
PACKAGE_DATA = list()

for directory in [ 'templates', 'static' ]:
    for root, dirs, files in os.walk( os.path.join( MODULE_NAME, directory )):
        for filename in files:
            PACKAGE_DATA.append("%s/%s" % ( root[len(MODULE_NAME)+1:], filename ))


def read( fname ):
    try:
        return open( os.path.join( os.path.dirname( __file__ ), fname ) ).read()
    except IOError:
        return ''


META_DATA = dict(
    name = PROJECT,
    version = VERSION,
    description = read('DESCRIPTION'),
    long_description = read('README.rst'),
    license=LICENSE,

    author = "Kirill Klenov",
    author_email = "horneds@gmail.com",

    url = "http://github.com/klen/django-netauth.git",

    keywords= 'auth django social',
    packages = find_packages(),
    package_data = { '': PACKAGE_DATA, },

    install_requires = [ 
        'python-openid', 
        'oauth2',
        'django-misc',
        ],
)

if __name__ == "__main__":
    setup( **META_DATA )
