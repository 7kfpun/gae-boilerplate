#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.ext import ndb

import logging

logger = logging.getLogger(__name__)


class Contact(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    phonenumber = ndb.StringProperty()
    body = ndb.TextProperty()
    sent = ndb.BooleanProperty(default=False)

    created_date = ndb.DateTimeProperty(auto_now_add=True)

    def __unicode__(self):
        return unicode('{0} - {1}'.format(self.subject, self.email))


class Guest(ndb.Model):
    name = ndb.StringProperty()
    age = ndb.IntegerProperty()

    @classmethod
    def all(cls):
        logger.info('all {}'.format(cls._class_name()))
        return cls.query()

    @classmethod
    def update(cls, id, name, age):
        guest = cls(id=id, name=name, age=age)
        guest.put()
        logger.info('Update: {}'.format(guest))
        return guest

    @classmethod
    def insert(cls, name, age):
        guest = cls(name=name, age=age)
        guest.put()
        logger.info('Insert: {}'.format(guest))
        return guest

    @classmethod
    def DeleteGuest(cls, id):
        key = ndb.Key(cls, id)
        key.delete()
        logger.info('Delete {} {}'.format(cls._class_name(), id))
