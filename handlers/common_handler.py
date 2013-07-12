import logging

logger = logging.getLogger(__name__)

from base import BaseHandler


class HelloHandler(BaseHandler):
    def get(self):
        config = self.app.config
        self.response.write('Hello, world!')


class DefaultHandler(BaseHandler):
    def get(self):
        config = self.app.config
        self.render_response('default.html')


class StarterHandler(BaseHandler):
    def get(self):
        config = self.app.config
        self.render_response('starter.html')


class SigninHandler(BaseHandler):
    def get(self):
        config = self.app.config
        self.render_response('signin.html')
