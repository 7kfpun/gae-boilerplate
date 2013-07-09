#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers import *

#This is the place where all of your URL mapping goes
urls_list = [
    (r'^/signin', SigninHandler),
    (r'^/hello', HelloHandler),
    (r'^/', DefaultHandler),
]

# lint_ignore=W0401
