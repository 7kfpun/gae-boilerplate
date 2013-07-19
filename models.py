#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.ext import ndb


class Contact(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    subject = ndb.TextProperty()
    body = ndb.TextProperty()

    created_date = ndb.DateProperty(auto_now_add=True)

    def __unicode__(self):
        return unicode('{0} - {1}'.format(self.subject, self.email))
