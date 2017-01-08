#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PET-Física UFRPE'
SITENAME = 'PET-Física UFRPE'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['images','posts','pages']

ARTICLE_URL = 'posts/{lang}/{date:%Y}-{date:%b}-{date:%d}-{slug}'
ARTICLE_SAVE_AS = 'posts/{lang}/{date:%Y}-{date:%b}-{date:%d}-{slug}.html'

PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{lang}/{slug}.html'

THEME = "iaxs"

TIMEZONE = 'America/Recife'
DEFAULT_LANG = 'pt-br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
	('Pelican', 'http://getpelican.com/'),
	('Python.org', 'http://python.org/'),
	('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
	('Facebook', 'https://www.facebook.com/profile.php?id=100005313284736&fref=ts'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
