#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Patricio Pérez'
AUTHOR_EMAIL = 'patricio.perez@ceinf.cl'
SITENAME = u"pato's corner"
SITEURL = 'http://alumnos.informatica.utem.cl/~pperez'
SITETAGLINE = 'Geeky bastard y algo busquilla'
SITEDESCR = 'Cosas que considero entretes, a veces me equivoco (?)'

TIMEZONE = 'America/Santiago'

DEFAULT_LANG = u'es-CL'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = [
    ('Seba', 'http://alumnos.informatica.utem.cl/~srocha/'),
    ('Python.org', 'http://python.org/')
]

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 200

THEME = 'lannisport'
TYPOGRIFY = True
PATH = 'content'

# STATIC_PATHS = ['images']

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins
PLUGIN_PATH = 'plugins'
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'pelican_gist'
           ]

# Settings personales
GOOGLE_ANALYTICS_CODE = 'UA-44982980-1'
GITHUB_URL = 'https://github.com/pperez/'
TWITTER_URL = 'http://twitter.com/janitux'
FACEBOOK_URL = 'http://facebook.com/janitux'
CONTACT_URL = 'about.html'
SITELOGO = 'images/me.png'
DISQUS_SHORTNAME = 'patoscorner'
CONTACT_URL = 'pages/acerca-de.html'