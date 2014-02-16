#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import Lesson
import json
import webapp2
#import time

import logging

logger = logging.getLogger(__name__)


def AsDict(lesson):
    return {
        'id': lesson.key.id(),
        'page': lesson.page,
        'content': lesson.content,
    }


def spoof_rest(func):
    """ Decorator to handle spoofing RESTful verbs """
    def inner(handler):
        params = handler.request.params
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


class ApiLessonHandler(RestHandler):

    #@spoof_rest
    def get(self, page=None):
        logger.info('Get')
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = '*'

        logger.debug("page {}".format(page))
        if page:
            lessons = Lesson.get(int(page))
        else:
            lessons = Lesson.all()

        r = [AsDict(lesson) for lesson in lessons]
        self.SendJson(r)

    #@spoof_rest
    def put(self):
        logger.info('Put')
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = '*'
        r = json.loads(self.request.body)
        lesson = Lesson.update(r['id'], r['page'], r['content'])
        r = AsDict(lesson)
        self.SendJson(r)

    def post(self):
        logger.info('Post')
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = '*'
        r = json.loads(self.request.body)
        lesson = Lesson.insert(r['page'], r['content'])
        r = AsDict(lesson)
        self.SendJson(r)

    def delete(self):
        logger.info('Delete')
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = '*'
        r = json.loads(self.request.body)
        Lesson.delete(r['id'])


class QueryHandler(RestHandler):

    def get(self):
        lessons = Lesson.all()
        r = [AsDict(lesson) for lesson in lessons]
        self.SendJson(r)


class UpdateHandler(RestHandler):

    def post(self):
        r = json.loads(self.request.body)
        lesson = Lesson.update(r['id'], r['page'], r['content'])
        r = AsDict(lesson)
        self.SendJson(r)


class InsertHandler(RestHandler):

    def post(self):
        r = json.loads(self.request.body)
        lesson = Lesson.insert(r['page'], r['content'])
        r = AsDict(lesson)
        self.SendJson(r)


class DeleteHandler(RestHandler):

    def post(self):
        r = json.loads(self.request.body)
        Lesson.delete(r['id'])
