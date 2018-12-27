#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Joe Seiler'
SITENAME = "Joe's Calepin"
SITEURL = 'https://joetechem.github.io'

THEME = "themes/nest"

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

#DEFAULT_DATE_FORMAT = u'%Y-%m-%d'

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
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/josef-seiler-315560111'),
          ('github', 'https://github.com/joetechem'),
          ('twitter', '#'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GITHUB_URL = u'https://github.com/joetechem'

# pelican-blue
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#SIDEBAR_DIGEST = 'Programmer and Web Developer'
#FAVICON = 'url-to-favicon'
#DISPLAY_PAGES_ON_MENU = True
#TWITTER_USERNAME = 'twitter-user-name'
#MENUITEMS = (('Blog', SITEURL),)

# Nest
NEST_HEADER_IMAGES = 'cloud-rain.jpg'
#NEST_HEADER_LOGO = '/images/orange-logo.png'
NEST_INDEX_HEAD_TITLE = u'Notebook'
NEST_INDEX_HEADER_TITLE = u'Notebook'
NEST_INDEX_HEADER_SUBTITLE = u'Learn something new'
NEST_INDEX_CONTENT_TITLE = u'Last Posts'