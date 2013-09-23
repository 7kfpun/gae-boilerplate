#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs import utils
from webapp2_extras.i18n import ngettext, gettext, lazy_gettext as _
from wtforms import fields, validators, Form


FIELD_MAXLENGTH = 50  # intended to stop maliciously long input


class FormTranslations(object):
    def gettext(self, string):
        return gettext(string)

    def ngettext(self, singular, plural, n):
        return ngettext(singular, plural, n)


class BaseForm(Form):
    def __init__(self, request_handler):
        super(BaseForm, self).__init__(request_handler.request.POST)

    def _get_translations(self):
        return FormTranslations()


# ==== Mixins ====
class PasswordConfirmMixin(BaseForm):
    password = fields.TextField(
        _('Password'),
        [validators.Required(),
         validators.Length(max=FIELD_MAXLENGTH, message=_(
             "Field cannot be longer than %(max)d characters."))])

    c_password = fields.TextField(
        _('Confirm Password'),
        [validators.Required(),
         validators.EqualTo('password', _('Passwords must match.')),
         validators.Length(max=FIELD_MAXLENGTH, message=_(
             "Field cannot be longer than %(max)d characters."))])


class UsernameMixin(BaseForm):
    username = fields.TextField(
        _('Username'),
        [validators.Required(),
         validators.Length(max=FIELD_MAXLENGTH, message=_(
             "Field cannot be longer than %(max)d characters.")),
         validators.regexp(utils.VALID_USERNAME_REGEXP, message=_(
             "Username invalid. Use only letters and numbers."))])


class NameMixin(BaseForm):
    name = fields.TextField(
        _('Name'),
        [validators.Length(max=FIELD_MAXLENGTH, message=_(
            "Field cannot be longer than %(max)d characters.")),
         validators.regexp(utils.NAME_LASTNAME_REGEXP, message=_(
             "Name invalid. Use only letters and numbers."))])

    last_name = fields.TextField(
        _('Last Name'),
        [validators.Length(max=FIELD_MAXLENGTH, message=_(
            "Field cannot be longer than %(max)d characters.")),
         validators.regexp(utils.NAME_LASTNAME_REGEXP, message=_(
             "Last Name invalid. Use only letters and numbers."))])


class EmailMixin(BaseForm):
    email = fields.TextField(
        _('Email'),
        [validators.Required(),
         validators.Length(min=8, max=FIELD_MAXLENGTH, message=_(
             "Field must be between %(min)d and %(max)d characters long.")),
         validators.regexp(utils.EMAIL_REGEXP, message=_(
             'Invalid email address.'))])


# ==== Forms ====
class ContactForm(EmailMixin):
    name = fields.TextField(
        _('Name'),
        [validators.Required(),
         validators.Length(max=FIELD_MAXLENGTH, message=_(
             "Field cannot be longer than %(max)d characters.")), ])
         #validators.regexp(utils.NAME_LASTNAME_REGEXP, message=_(
             #"Name invalid. Use only letters and numbers."))])

    subject = fields.TextField(
        _('Message'),
        [validators.Required(),
         validators.Length(max=256)])

    body = fields.TextAreaField(
        _('Body'),
        [validators.Required(),
         validators.Length(max=65536)])
