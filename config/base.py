""" Project base settings """
import os

base_config = {
    'default_locale': 'en_US',
    'locales': ['en_US'],  # , 'zh_TW', 'zh_CN', 'th_TH'],
    'PROJECT_ROOT': os.path.dirname(os.path.dirname(__file__)),
}
base_config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}
