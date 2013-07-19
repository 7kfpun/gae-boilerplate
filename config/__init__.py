"""
This configuration file loads environment's specific config settings
for the application.
"""
import os

import logging

from .base import base_config

logger = logging.getLogger(__name__)

if "SERVER_SOFTWARE" in os.environ:
    if os.environ['SERVER_SOFTWARE'].startswith('Dev'):
        from config.localhost import config

    elif os.environ['SERVER_SOFTWARE'].startswith('Google'):
        from config.production import config
else:
    from config.testing import config

config.update(base_config)
config = config

logger.info(
    'GAE is running on {0}, with config {1}'.format(
        os.environ['SERVER_SOFTWARE'], config)
)
