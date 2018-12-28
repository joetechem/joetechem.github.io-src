#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Joe Seiler'
SITENAME = 'Calepin Joe'
SITEURL = 'https://joetechem.github.io'

THEME = "themes/nest"

PATH = 'content'

#TIMEZONE = 'America/New_York'
TIMEZONE = 'US/Eastern'

#DEFAULT_LANG = 'en'
DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (('Home', 'https://joetechem.github.io'),
             ('About', 'https://joetechem.github.io'))

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'))

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/josef-seiler-315560111'),
          ('github', 'https://github.com/joetechem'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GITHUB_URL = 'https://github.com/joetechem'

# pelican-blue
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#SIDEBAR_DIGEST = 'Programmer and Web Developer'
#FAVICON = 'url-to-favicon'
#DISPLAY_PAGES_ON_MENU = True
#TWITTER_USERNAME = 'twitter-user-name'
#MENUITEMS = (('Blog', SITEURL),)

# Nest
NEST_HEADER_IMAGES = 'raspberry-pi-stock.jpg'
NEST_HEADER_LOGO = '/images/notebook-logo.jpg'
NEST_INDEX_HEAD_TITLE = 'Calepin Joe'
NEST_INDEX_HEADER_TITLE = 'Calepin Joe'
NEST_INDEX_HEADER_SUBTITLE = 'Learn something new'
NEST_INDEX_CONTENT_TITLE = 'Last Posts'