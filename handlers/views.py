#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from webapp2_extras.i18n import lazy_gettext as _

from forms import ContactForm
from models import Contact, Lesson

import logging

logger = logging.getLogger(__name__)

from base import BaseHandler
from mails import send_contact_mail


class HomeHandler(BaseHandler):
    def get(self, locale=None):
        self.set_locale(locale)
        self.render_response('index.html', locale=locale)


class LessonHandler(BaseHandler):
    def get(self, page=None):
        page = page or 1
        lesson = Lesson.get(page)
        logger.debug(lesson)
        if lesson:
            self.render_response('lesson.html', lesson=lesson[0])
        else:
            self.redirect("/")


class SigninHandler(BaseHandler):
    def get(self):
        self.render_response('signin.html')


class ContactHandler(BaseHandler):
    def get(self):
        params = {
            'form': ContactForm(self),
        }
        self.render_response('contact.html', **params)

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
                phonenumber=self.request.get('phonenumber'),
                body=self.request.get('body'),
            )
            logger.info(contact)
            contact.put()
            send_contact_mail(self)
        else:
            self.render_response('contact.html', **params)


class CheckingHandler(BaseHandler):
    def get(self):
        self.response.write(self.request)
        self.response.write(self.locales)
