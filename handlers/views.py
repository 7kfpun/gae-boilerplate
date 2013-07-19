#!/usr/bin/env python
# -*- coding: utf-8 -*-
from forms import ContactForm
from google.appengine.api import users
from models import Contact

import logging

logger = logging.getLogger(__name__)

from base import BaseHandler


class HelloHandler(BaseHandler):
    def get(self):
        self.response.write(self.config)


class DefaultHandler(BaseHandler):
    def get(self):
        params = {
            'form': ContactForm(self),
        }
        self.render_response('default.html', **params)

    def post(self):
        form = ContactForm(self)
        params = {
            'form': form,
        }
        self.response.write(form.validate())
        self.render_response('default.html', **params)


class StarterHandler(BaseHandler):
    def get(self):
        self.render_response('starter.html')


class SigninHandler(BaseHandler):
    def get(self):
        self.render_response('signin.html')
