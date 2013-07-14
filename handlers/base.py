import jinja2
import json
import os
import webapp2
from webapp2_extras import i18n

from config import config

import logging

logger = logging.getLogger(__name__)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), "../templates"),
    ),
    extensions=['jinja2.ext.i18n', 'jinja2.ext.autoescape'])

JINJA_ENVIRONMENT.install_gettext_translations(i18n)


class BaseHandler(webapp2.RequestHandler):
    """BaseHandler which will be inherited all other handlers
    it should implement the most common functionality
    required by all handlers
    """

    def __init__(self, request, response):
        self.initialize(request, response)
        self.config = config

    def render_response(self, _template, **context):
        locale = self.request.GET.get('locale', 'en_US')
        i18n.get_i18n().set_locale('zh_tw')
        logger.info('locale is {0}'.format(locale))

        template = JINJA_ENVIRONMENT.get_template(_template)
        self.response.write(template.render(**context))

    def render_json(self, obj):
        rv = json.dumps(obj)
        self.response.headers.content_type = 'application/json'
        self.response.write(rv)
