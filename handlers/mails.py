#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from google.appengine.api import mail
from webapp2_extras.json import json

import logging

logger = logging.getLogger(__name__)

from models import Contact
from base import BaseHandler


class MailContactHandler(BaseHandler):
    def get(self):
        contacts = Contact.query(Contact.sent != True)
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
                sender="Example.com Support <support@example.com>",
                to="Albert Johnson <Albert.Johnson@example.com>",
                subject="You have {0} new contacts".format(count),
                body=message
            )

            self.response.write(message)
            logger.info(
                'Send daily mail success, {0} new contacts'.format(count))

            for contact in contacts:
                contact.sent = True
                contact.put()
