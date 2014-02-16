#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from google.appengine.api import mail
from google.appengine.ext import ndb
from webapp2_extras.json import json

from models import Contact
from base import BaseHandler

import logging

logger = logging.getLogger(__name__)


def send_contact_mail(self):
    contacts = Contact.query(Contact.sent != True).order(Contact.created_date)
    count = contacts.count()
    if count:
        datetime_handler = lambda obj: obj.isoformat() \
            if isinstance(obj, datetime) else None
        message = json.dumps(
            [contact.to_dict() for contact in contacts],
            default=datetime_handler,
            indent=4
        )

        mail.send_mail(
            sender="Thaiinhk.com Support <710kfpun@gmail.com>",
            to="Thai in HK <710kfpun@gmail.com>",
            subject="You have {0} new contact(s)".format(count),
            body=message
        )

        self.response.write(message)
        logger.info(
            'Send daily mail success, {0} new contacts'.format(count))

        put_list = []
        for contact in contacts:
            contact.sent = True
            put_list.append(contact)

        ndb.put_multi(put_list)


class MailContactHandler(BaseHandler):
    def get(self):
        send_contact_mail(self)


class MailAllHandler(BaseHandler):
    def get(self):
        contacts = Contact.query().order(Contact.created_date)
        datetime_handler = lambda obj: obj.isoformat() \
            if isinstance(obj, datetime) else None
        self.render_json(
            [contact.to_dict() for contact in contacts],
            default=datetime_handler,
        )
        logger.info('Check all {} contact(s)'.format(contacts.count()))


# lint_ignore=E712
