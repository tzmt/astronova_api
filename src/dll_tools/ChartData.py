from logging import getLogger
import json

logger = getLogger(__name__)
"""
A class created by the ChartManager singleton representing chart data for a given date, time, and location.
"""


class ChartData:
    def __init__(self, local_datetime, utc_datetime, julian_day):
        self.local_datetime = local_datetime
        self.utc_datetime = utc_datetime
        self.julian_day = julian_day
        self.sidereal_framework = None
        self.cusps_longitude = None
        self.angles_longitude = None

        # Ecliptical longitude, celestial latitude, distance, speed in long, speed in lat, speed in dist
        self.planets_ecliptic = None

        # House placement, decimal longitude (out of 360*)
        self.planets_mundane = None

        # Decimal longitude (out of 360*)
        self.planets_right_ascension = None

    def get_ecliptical_coords(self):
        coords = dict()
        for planet in self.planets_ecliptic.keys():
            coords[planet] = self.planets_ecliptic[planet][0]
        return coords

    def get_mundane_coords(self):
        coords = dict()
        for planet in self.planets_mundane.keys():
            coords[planet] = self.planets_mundane[planet][1]
        return coords

    def get_right_ascension_coords(self):
        return self.planets_right_ascension

    def get_angles_longitude(self):
        return self.angles_longitude

    def get_cusps_longitude(self):
        return self.cusps_longitude

    def jsonify_chart(self):
        j = dict()
        j['ecliptical'] = self.get_ecliptical_coords()
        j['mundane'] = self.get_mundane_coords()
        j['right_ascension'] = self.get_right_ascension_coords()
        j['angles'] = self.get_angles_longitude()
        j['cusps'] = self.get_cusps_longitude()
        j['local_datetime'] = self.local_datetime
        j['utc_datetime'] = self.utc_datetime
        j['julian_day'] = self.julian_day
        j['lst'] = self.sidereal_framework.lst or ''
        j['ramc'] = self.sidereal_framework.ramc or ''
        j['obliquity'] = self.sidereal_framework.obliquity or ''
        j['svp'] = self.sidereal_framework.svp or ''
        j['longitude'] = self.sidereal_framework.geo_longitude or ''
        j['latitude'] = self.sidereal_framework.geo_latitude or ''

        return json.dumps(j)

    def __str__(self):
        return str({
            'Date': str(self.local_datetime),
            'Sidereal framework': str(self.sidereal_framework),
            'Ecliptical': self.get_ecliptical_coords(),
            'Mundane': self.get_mundane_coords(),
            'RA': self.get_right_ascension_coords(),
            'Cusps': self.get_cusps_longitude(),
            'Angles': self.get_angles_longitude(),
        })
