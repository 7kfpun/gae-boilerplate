import logging

logger = logging.getLogger(__name__)

from base import BaseHandler


class HelloHandler(BaseHandler):
    def get(self):
        self.response.write(self.app.config)


class HomeHandler(BaseHandler):
    def get(self):
        self.render_response('index.html')


class StarterHandler(BaseHandler):
    def get(self):
        self.render_response('starter.html')


class SigninHandler(BaseHandler):
    def get(self):
        self.render_response('signin.html')
