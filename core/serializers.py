"""
Views serializers classes - Provider and ServiceArea
"""
# coding=utf-8

from rest_framework import serializers # pylint: disable=import-error
from .models import Provider, ServiceArea

__author__ = "Rafael Lucas"
__version__ = "1.0"
__maintainer__ = "Rafael Lucas"
__email__ = "rafael@flightpooling.com"

class ProviderSerializer(serializers.ModelSerializer):
    """ Serializer - Provider class """
    class Meta:
        """ Serializer - Provider META class """
        model = Provider
        fields = '__all__'


class ServiceAreaSerializer(serializers.ModelSerializer):
    """ Serializer - Service area class """
    class Meta:
        """ Serializer - Service area META class """
        model = ServiceArea
        fields = '__all__'
