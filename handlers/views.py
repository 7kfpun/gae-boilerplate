#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
from forms import ContactForm
from models import Contact
from webapp2_extras.i18n import lazy_gettext as _

import logging

logger = logging.getLogger(__name__)

from base import BaseHandler


class HelloHandler(BaseHandler):
    def get(self):
        self.response.write(self.app.config)


class HomeHandler(BaseHandler):
    def get(self):
        self.render_response('index.html')


class StarterHandler(BaseHandler):
    def get(self):
        self.render_response('starter.html')


class SigninHandler(BaseHandler):
    def get(self):
        self.render_response('signin.html')


class ContactHandler(BaseHandler):
    def get(self):
        params = {
            'form': ContactForm(self),
        }
        self.render_response('contact.html', **params)
        self.response.write(self.request)

    def post(self):
        form = ContactForm(self)
        params = {
            'form': form,
        }
        self.response.write(form.validate())
        if form.validate():
            contact = Contact(
                name=self.request.get('name'),
                email=self.request.get('email'),
                subject=self.request.get('subject'),
                body=self.request.get('body'),
            )
            contact.put()
        self.render_response('contact.html', **params)


class CheckingHandler(BaseHandler):
    def get(self):
        self.response.write(self.request)

        self.response.write(self.locales)
