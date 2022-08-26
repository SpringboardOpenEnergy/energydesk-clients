from datetime import datetime, timedelta, timezone
import pytz
from dateutil import parser

def localize_datetime(dt,  loczone="UTC"):
    timezone = pytz.timezone(loczone)
    d_aware = timezone.localize(dt)
    return d_aware

def convert_timezone(dt,  loczone="UTC"):
    timezone = pytz.timezone(loczone)
    converted = dt.astimezone(timezone)
    return converted

def localize_strtime(strtime, loczone):
    unaware_dt = parser.isoparse(strtime)
    return localize_datetime(unaware_dt)

def convert_datime_to_utcstr(dt):
    dtutc=convert_timezone(dt)
    s_dt = dtutc.strftime('%Y-%m-%dT%H:%M:%S+00:00')
    return s_dt

def convert_datime_to_locstr(dt, loczone="Europe/Oslo"):
    dtutc=localize_datetime(dt, loczone)
    s_dt = dtutc.strftime('%Y-%m-%dT%H:%M:%S+00:00')
    return s_dt