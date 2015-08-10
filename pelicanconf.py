#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matias S.'
SITENAME = u'schertel.co'
SITESUBTITLE = u'My kung fu is stronger than yours'
SITEURL = ''

# Theme
THEME = 'notmyidea'

# Plugins
PLUGIN_PATHS = ['plugins', ]
PLUGINS = ['sitemap', 'optimize_images']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

LOCALE = ('en', 'en_US.utf8',
          'pt', 'pt_BR.utf8',)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Curriculum', 'http://schertel.co/'),
         ('Menvia', 'http://menvia.com/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/flatlining'),
          ('github', 'http://github.com/flatlining'),)

TWITTER_USERNAME = 'flatlining'
#GITHUB_URL = 'https://github.com/flatlining/'

# Analytics
GOOGLE_ANALYTICS = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Typogrify
TYPOGRIFY = True

# Extra
STATIC_PATHS = ['images', 'extra/favicon.ico', 'extra/.htaccess']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/.htaccess': {'path': '.htaccess'},}

# Pagination
# https://github.com/getpelican/pelican/issues/1137
# https://github.com/getpelican/pelican/issues/1615
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),)

# Articles
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%m}/{slug}/{lang}/'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL + 'index.html'

# Pages
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_LANG_URL = 'pages/{slug}/{lang}/'
PAGE_LANG_SAVE_AS = PAGE_LANG_URL + 'index.html'

# Archives
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

# Author
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = AUTHOR_URL + 'index.html'
AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = AUTHORS_URL + 'index.html'

# Category
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'
CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = CATEGORIES_URL + 'index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = TAGS_URL + 'index.html'
