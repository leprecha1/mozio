"""
Django Model - Core
Provider and ServiceArea classes
"""
# coding=utf-8

from __future__ import unicode_literals
from django.db import models # pylint: disable=import-error
from django_mysql.models import JSONField, Model # pylint: disable=import-error

__author__ = "Rafael Lucas"
__version__ = "1.0"
__maintainer__ = "Rafael Lucas"
__email__ = "rafael@flightpooling.com"

class Provider(Model):
    """
    Class Provider - Mozio Challenge

    Args:
        name     (str): Provider name.
        email    (str): Provider email.
        phone    (str): Provider phone number.
        language (str): Provider language - 3 char - i.e: EN.
        currency (str): Provider currency - 4 char - i.e: GBP.
    """
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    language = models.CharField(max_length=3)
    currency = models.CharField(max_length=4)

    class Meta:
        """ Provider meta class """
        verbose_name = u'Provider'
        verbose_name_plural = u'Providers'

    def __str__(self):
        return self.name

class ServiceArea(Model):
    """
    Class ServiceArea - Mozio Challenge

    Args:
        name        (str): Service Area name.
        price       (str): Service Area price.
        provider    (<provider_class>): Service Area provider.
        area        (JSON object): Service Are GEOJSON polygon notation.
    """
    name = models.CharField(max_length=100)
    price = models.FloatField()
    provider = models.ForeignKey(Provider, verbose_name="Provider", on_delete=models.CASCADE)
    area = JSONField()

    class Meta:
        """ ServiceArea meta class """
        verbose_name = u'ServiceArea'
        verbose_name_plural = u'ServiceArea'

    def __str__(self):
        return self.name
