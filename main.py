#!/usr/bin/env python
#
import webapp2
import logging

# adjust library path before any other module gets imported...
# don't comment or delete
import fix_path

from urls import (
    admin_urls_list,
    api_urls_list,
    urls_list,
)
from config import config

logger = logging.getLogger(__name__)

app = webapp2.WSGIApplication(
    urls_list,
    config=config,
    debug=config.get('debug', False),
)

api_app = webapp2.WSGIApplication(
    api_urls_list,
    config=config,
    debug=config.get('debug', False),
)

admin_app = webapp2.WSGIApplication(
    admin_urls_list,
    config=config,
    debug=config.get('debug', False),
)
