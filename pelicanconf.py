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

DEFAULT_LANG = 'en'

#DEFAULT_DATE_FORMAT = '%Y-%m-%d'
#DEFAULT_DATE_FORMAT = '{slug}Y-{slug}m-{slug}d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#MENUITEMS = (('Home', 'https://joetechem.github.io'), ('About', 'https://joetechem.github.io'))
MENUITEMS = [('Home', 'https://joetechem.github.io'), ('About', 'https://joetechem.github.io')]


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
NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [('Archives', '/archives.html'),('Tags','/tags.html')]

NEST_HEADER_IMAGES = 'raspberry-pi-stock.jpg'
NEST_HEADER_LOGO = '/images/notebook-logo.jpg'
NEST_INDEX_HEAD_TITLE = u'Calepin Joe'
NEST_INDEX_HEADER_TITLE = u'Calepin Joe'
NEST_INDEX_HEADER_SUBTITLE = u'Learn something new'
NEST_INDEX_CONTENT_TITLE = u'Last Posts'
NEST_COPYRIGHT = u'&copy; blogname 2018'