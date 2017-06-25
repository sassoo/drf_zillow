"""
    utils
    ~~~~~

    Helper methods for communicating with the Zillow XML API.

    ZILLOW_TABLE contains the name of the property in the
    zillow API (key) & a value that we much prefer
"""

import requests

from django.conf import settings
from lxml import etree


BASE_URL = 'https://www.zillow.com'
DEEP_SEARCH_URL = '%s/webservice/GetDeepSearchResults.htm' % BASE_URL

ZILLOW_KEY = settings.ZILLOW_KEY

ZILLOW_TABLE = {
    'bathrooms': 'bathrooms',
    'bedrooms': 'bedrooms',
    'finishedSqFt': 'livingSqft',
    'lastSoldDate': 'lastSoldDate',
    'lastSoldPrice': 'lastSoldPrice',
    'lotSizeSqFt': 'totalSqft',
    'useCode': 'useCode',
    'yearBuilt': 'yearBuilt',
    'zestimate/amount': 'value',
    'zestimate/last-updated': 'lastUpdated',
    'homedetails': 'zillowLink',
}


def _run_query(url, params):
    """ Query a Zillow API & return the XML tree object """

    try:
        res = requests.get(DEEP_SEARCH_URL, params=params)
        res.raise_for_status()
        return etree.fromstring(res.content)  # pylint: disable=no-member
    except:
        raise IOError('error contacting zillow')


def deep_search(street, citystatezip):
    """ Get the details of an address from the Zillow deep search API

    Zillow is an XML based API that requires query params of
    a certain type. The format is as follows:

        'address':      '2660 Forest Run Drive',
        'citystatezip': 'Melbourne Fl 32951',

    :raises:
        IOError in the event that communicating with zillow
        fails for any reason.
    :returns:
        A python dictionary of zillow key vals or None if
        nothing is found in Zillow
    """

    params = {
        'address': street,
        'citystatezip': citystatezip,
        'zws-id': ZILLOW_KEY,
    }
    ret = {}
    tree = _run_query(DEEP_SEARCH_URL, params)

    for z_key, key in ZILLOW_TABLE.items():
        try:
            ret[key] = tree.find('.//%s' % z_key).text
            ret[key] = int(float(ret[key]))
        except BaseException:
            continue

    if ret.get('lastSoldPrice'):
        ret['lastSoldPricePretty'] = '$' + '{:,}'.format(ret['lastSoldPrice'])
    if ret.get('lastUpdated') == '12/31/1969':
        del ret['lastUpdated']
    if ret.get('value'):
        ret['valuePretty'] = '$' + '{:,}'.format(ret['value'])
    if ret.get('zillowLink'):
        return ret

    return None