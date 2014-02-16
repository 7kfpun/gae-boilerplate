#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import Guest
import json
import webapp2
#import time

import logging

logger = logging.getLogger(__name__)


def AsDict(guest):
    return {'id': guest.key.id(), 'name': guest.name, 'age': guest.age}


def spoof_rest(func):
    """ Decorator to handle spoofing RESTful verbs """
    def inner(handler):
        params = handler.request.params
        logger.debug(dir(handler))
        if 'http_verb' in params:
            if params['http_verb'] == 'PUT':
                handler.put()
            elif params['http_verb'] == 'DELETE':
                handler.delete()
    return inner


class RestHandler(webapp2.RequestHandler):

    def dispatch(self):
        #time.sleep(1)
        super(RestHandler, self).dispatch()

    def SendJson(self, r):
        self.response.headers['content-type'] = 'text/plain'
        self.response.write(json.dumps(r))


class GuestHandler(RestHandler):

    @spoof_rest
    def get(self):
        logger.info('Get')
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = '*'
        guests = Guest.all()
        r = [AsDict(guest) for guest in guests]
        self.SendJson(r)

    @spoof_rest
    def put(self):
        logger.info('Put')
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = '*'
        r = json.loads(self.request.body)
        guest = Guest.update(r['id'], r['name'], r['age'])
        r = AsDict(guest)
        self.SendJson(r)

    def post(self):
        logger.info('Post')
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = '*'
        r = json.loads(self.request.body)
        guest = Guest.insert(r['name'], r['age'])
        r = AsDict(guest)
        self.SendJson(r)

    def delete(self):
        logger.info('Delete')
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = '*'
        r = json.loads(self.request.body)
        Guest.delete(r['id'])


class QueryHandler(RestHandler):

    def get(self):
        guests = Guest.all()
        r = [AsDict(guest) for guest in guests]
        self.SendJson(r)


class UpdateHandler(RestHandler):

    def post(self):
        r = json.loads(self.request.body)
        guest = Guest.update(r['id'], r['name'], r['age'])
        r = AsDict(guest)
        self.SendJson(r)


class InsertHandler(RestHandler):

    def post(self):
        r = json.loads(self.request.body)
        guest = Guest.insert(r['name'], r['age'])
        r = AsDict(guest)
        self.SendJson(r)


class DeleteHandler(RestHandler):

    def post(self):
        r = json.loads(self.request.body)
        Guest.delete(r['id'])
