from babel import Locale
from hashlib import md5
from google.appengine.api import urlfetch
from google.appengine.api.urlfetch_errors import DownloadError
from webapp2_extras import i18n
import re

import logging

logger = logging.getLogger(__name__)

def parse_accept_language_header(string, pattern='([a-zA-Z]{1,8}(-[a-zA-Z0-9]{1,8})?)\s*(;\s*q\s*=\s*(1|0\.[0-9]+))?'):
    """
    Parse a dict from an Accept-Language header string
    (see http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html)
    example input: en-US,en;q=0.8,es-es;q=0.5
    example output: {'en_US': 100, 'en': 80, 'es_ES': 50}
    """
    res = {}
    if not string:
        return None
    for match in re.finditer(pattern, string):
        if None == match.group(4):
            q = 1
        else:
            q = match.group(4)
        l = match.group(1).replace('-', '_')
        if len(l) == 2:
            l = l.lower()
        elif len(l) == 5:
            l = l.split('_')[0].lower() + "_" + l.split('_')[1].upper()
        else:
            l = None
        if l:
            res[l] = int(100 * float(q))
    return res


def get_territory_from_ip(self):
    """
    call: get_territory_from_ip(self.request)

    Detect the territory code derived from IP Address location
    Returns US, CA, CL, AR, etc.
    self: self object

    Uses lookup service http://geoip.wtanaka.com/cc/<ip>
    You can get a flag image given the returned territory
        with http://geoip.wtanaka.com/flag/<territory>.gif
        example: http://geoip.wtanaka.com/flag/us.gif
    """
    territory = None
    try:
        cook_territoy = self.request.cookies.get('territory', None)
        if cook_territoy is not None:
            return cook_territoy

        result = urlfetch.fetch("http://geoip.wtanaka.com/cc/%s" % self.request.remote_addr, deadline=0.8) # tweak deadline if necessary
        if result.status_code == 200:
            fetch = result.content
            if len(str(fetch)) < 3:
                territory = str(fetch).upper()
                self.response.set_cookie('territory', territory, max_age=15724800)
            else:
                logger.warning("Ups, geoip.wtanaka.com is not working. Look what it returns: %s" % str(fetch) )
        else:
            logger.warning("Ups, geoip.wtanaka.com is not working. Status Code: %s" % str(result.status_code) )
    except DownloadError:
        logger.warning("Couldn't resolve http://geoip.wtanaka.com/cc/%s"% self.request.remote_addr)
    return territory


def get_locale_from_accept_header(request):
    """
    Detect locale from request.header 'Accept-Language'
    Locale with the highest quality factor that most nearly matches our
    config.locales is returned.
    self: self object

    Note that in the future if
        all User Agents adopt the convention of sorting quality factors in descending order
        then the first can be taken without needing to parse or sort the accept header
        leading to increased performance
        (see http://lists.w3.org/Archives/Public/ietf-http-wg/2012AprJun/0473.html)
    """
    header = request.headers.get("Accept-Language", '')
    parsed = parse_accept_language_header(header)
    if parsed is None:
        return None
    locale_list_sorted_by_q = sorted(parsed.iterkeys(), reverse=True)
    locale = Locale.negotiate(locale_list_sorted_by_q, request.app.config.get('locales'), sep='_')
    return str(locale)


def get_signiture(text):
    return md5(text).hexdigest()
