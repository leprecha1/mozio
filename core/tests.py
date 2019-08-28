"""
Django Tests / Unittest - Core
"""
# coding=utf-8

from django.test import TestCase # pylint: disable=import-error
from model_mommy import mommy # pylint: disable=import-error
from core.models import Provider, ServiceArea

__author__ = "Rafael Lucas"
__version__ = "1.0"
__maintainer__ = "Rafael Lucas"
__email__ = "rafael@flightpooling.com"

class TestProvider(TestCase):
    """ Unittest for Provider Class objects"""
    def setUp(self):
        """ SetUp for Unittest - Provider Class objects"""
        self.provider = mommy.make(Provider,
                                   name='Provider 1',
                                   email='provider@prvd.com',
                                   phone='+55xxyyy-0000',
                                   language='PT',
                                   currency='BRL')

    def test_provider_creation(self):
        """ Unittest for Provider Class objects - creation """
        self.assertTrue(isinstance(self.provider, Provider))
        self.assertEquals(self.provider.__str__(), self.provider.name)

class TestServiceArea(TestCase):
    """ Unittest for ServiceArea Class objects"""
    def setUp(self):
        """ SetUp for Unittest - ServiceArea Class objects"""
        self.provider = mommy.make(Provider,
                                   name='Provider 1',
                                   email='provider@prvd.com',
                                   phone='+55xxyyy-0000',
                                   language='PT',
                                   currency='BRL')

        self.service_area = mommy.make(ServiceArea,
                                       name='Service Area 1',
                                       price=40000.0,
                                       provider=self.provider,
                                       area={
                                           "type": "Feature",
                                           "properties": {
                                               "name": "Bermuda Triangle",
                                               "area": 1150180
                                           },
                                           "geometry": {
                                               "type": "Polygon",
                                               "coordinates": [
                                                   [
                                                       [-64.73, 32.31],
                                                       [-80.19, 25.76],
                                                       [-66.09, 18.43],
                                                       [-64.73, 32.31]
                                                   ]
                                               ]
                                           }
                                       })

    def test_music_creation(self):
        """ Unittest for ServiceArea Class objects - creation """
        self.assertTrue(isinstance(self.service_area, ServiceArea))
        self.assertEquals(self.service_area.__str__(), self.service_area.name)
