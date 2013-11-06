from babel import Locale
from google.appengine.api import memcache

import jinja2
import json
import os
#from pytz.gae import pytz
import webapp2
from webapp2_extras import i18n, sessions

from .helpers import (
    get_locale_from_accept_header,
    #get_territory_from_ip,
    #parse_accept_language_header,
    get_signiture,
)

import logging

logger = logging.getLogger(__name__)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), "../templates"),
    ),
    extensions=[
        'jinja2.ext.i18n',
        'jinja2.ext.autoescape',
    ]
)

JINJA_ENVIRONMENT.install_gettext_translations(i18n)


class BaseHandler(webapp2.RequestHandler):
    """BaseHandler which will be inherited all other handlers
    it should implement the most common functionality
    required by all handlers
    """

    def __init__(self, request, response):
        self.initialize(request, response)
        self.locale = self.set_locale()

    @property
    def locales(self):
        """
        returns a dict of locale codes to locale display names in both
        the current locale and the localized locale
        example: if the current locale is es_ES then
        locales['en_US'] = 'Ingles (Estados Unidos) - English (United States)'
        """
        if not self.app.config.get('locales'):
            return None
        locales = {}
        for l in self.app.config.get('locales'):
            current_locale = Locale.parse('en_US')
            language = current_locale.languages[l.split('_')[0]]
            territory = current_locale.territories[l.split('_')[1]]
            localized_locale_name = Locale.parse(l).display_name.capitalize()
            locales[l] = language.capitalize() \
                + " (" + territory.capitalize() + ") - " \
                + localized_locale_name
        return locales

    def set_locale(self, force=None):
        locales = self.app.config.get('locales')
        # disable i18n if config.locales array is empty or None
        if not locales:
            return None
        # 1. force locale if provided
        locale = force
        if locale not in locales:
            # 2. retrieve locale from url query string
            locale = self.request.get("hl", None)
            if locale not in locales:
                # 3. retrieve locale from cookie
                locale = self.request.cookies.get('hl', None)
                if locale not in locales:
                    # 4. retrieve locale from accept language header
                    locale = get_locale_from_accept_header(self.request)
                    if locale not in locales:
                        # 5. detect locale from IP address location
                        #territory = get_territory_from_ip(self) or 'ZZ'
                        #locale = str(Locale.negotiate(territory, locales))
                        if locale not in locales:
                            # 6. use default locale
                            locale = self.request.GET.get('locale', 'en_US')

        i18n.get_i18n().set_locale(locale)
        logger.info('locale is {0}'.format(locale))
        # save locale in cookie with 26 weeks expiration (in seconds)
        self.response.set_cookie('hl', locale, max_age=15724800)
        return locale

    def render_response(self, _template, cache_time=0, **context):
        if cache_time:
            logger.info('cache used for {0} s'.format(cache_time))
            # TODO: add session
            transliterated_text = _template + json.dumps(context.values())
            signature = get_signiture(transliterated_text)
            logger.debug('cache key {0}'.format(signature))

            rendered_page = memcache.get('page {0}'.format(signature))
            if not rendered_page:
                template = JINJA_ENVIRONMENT.get_template(_template)
                rendered_page = template.render(**context)

                if not memcache.add(
                        'page {0}'.format(signature),
                        rendered_page, cache_time):
                    logging.error('Memcache set failed.')
        else:
            template = JINJA_ENVIRONMENT.get_template(_template)
            rendered_page = template.render(**context)

        self.response.write(rendered_page)

    def render_json(self, obj):
        rv = json.dumps(obj)
        self.response.headers.content_type = 'application/json'
        self.response.write(rv)

    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()
