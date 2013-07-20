#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers import *


#This is the place where all of your URL mapping goes
urls_list = [
    (r'^/hello', HelloHandler),
    (r'^/', HomeHandler),
    (r'^/starter', StarterHandler),
    (r'^/signin', SigninHandler),
    (r'^/contact', ContactHandler),

    # admin urls
    (r'^/checking', CheckingHandler),
    (r'^/mail/contact', MailContactHandler),
]


# lint_ignore=W0401
