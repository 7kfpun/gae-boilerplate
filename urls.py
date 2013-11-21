#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers import *


#This is the place where all of your URL mapping goes
urls_list = [
    (r'^/hello/$', HelloHandler),
    (r'^/$', HomeHandler),
    #(r'^/starter', StarterHandler),
    #(r'^/signin', SigninHandler),
    (r'^/contact/$', ContactHandler),
    (r'^/sitemap.xml$', SitemapHandler),
]

admin_urls_list = [
    # admin urls, remember to configure in app.yaml
    (r'^/mail/all/$', MailAllHandler),
    (r'^/mail/contact/$', MailContactHandler),
]

# lint_ignore=W0401
