import os
import pygeoip
import logging


logger = logging.getLogger(__name__)


def get_record(ip):
    gi = pygeoip.GeoIP(os.path.join(os.path.dirname(__file__),
                                    'GeoLiteCity.dat'))
    record = gi.record_by_addr(str(ip))
    return record


def get_city_country(ip):
    record = get_record(ip)
    if record is None:
        if ip[:3] != "172":
            logger.info("IP missing from geolite database: %s", ip)
        return "Unknown"
    else:
        return u'{}, {}'.format(record['city'] or 'Unknown',
                                record['country_name'] or 'Unknown')
