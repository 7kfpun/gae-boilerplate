#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers import *
from handlers.base import BaseHandler


#This is the place where all of your URL mapping goes
urls_list = [
    (r'^/hello', HelloHandler),
    (r'^/', DefaultHandler),
    (r'^/starter', StarterHandler),
    (r'^/signin', SigninHandler),
]

# lint_ignore=W0401
