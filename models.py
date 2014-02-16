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


class Lesson(ndb.Model):
    page = ndb.IntegerProperty()
    content = ndb.TextProperty()

    @classmethod
    def get(cls, page):
        logger.info('get {}: {}'.format(cls._class_name(), page))
        lesson = cls.query(cls.page == int(page))
        return [l for l in lesson]

    @classmethod
    def all(cls, *kwds):
        logger.info('all {}'.format(cls._class_name()))
        return cls.query(*kwds).order(cls.page)

    @classmethod
    def update(cls, id, page, content):
        lesson = cls(id=id, page=page, content=content)
        lesson.put()
        logger.info('Update: {}'.format(lesson))
        return lesson

    @classmethod
    def insert(cls, page, content):
        lesson = cls(page=page, content=content)
        lesson.put()
        logger.info('Insert: {}'.format(lesson))
        return lesson

    @classmethod
    def delete(cls, id):
        key = ndb.Key(cls, id)
        key.delete()
        logger.info('Delete {} {}'.format(cls._class_name(), id))
