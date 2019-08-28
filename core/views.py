"""
Django Views - Core
"""
# coding=utf-8

from json import loads
from django_filters import rest_framework as filters # pylint: disable=import-error
from rest_framework import generics # pylint: disable=import-error
from shapely.geometry import shape, Point # pylint: disable=import-error
from .models import ServiceArea, Provider
from .serializers import ProviderSerializer, ServiceAreaSerializer # pylint: disable=import-error

__author__ = "Rafael Lucas"
__version__ = "1.0"
__maintainer__ = "Rafael Lucas"
__email__ = "rafael@flightpooling.com"

class ProviderList(generics.ListCreateAPIView):
    """
    Class ProviderList - views - Django DRF - Mozio Challenge
    provides Provider list and creation a new provider object
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Class ProviderDetail - views - Django DRF - Mozio Challenge
    provides Provider object update, deletion and object overview
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ServiceAreaList(generics.ListCreateAPIView):
    """
    Class ServiceAreaList - views - Django DRF - Mozio Challenge
    provides Service Area list and creation a new ServiceArea object
    """
    serializer_class = ServiceAreaSerializer

    def get_queryset(self):
        queryset = ServiceArea.objects.all()
        lat = self.request.query_params.get('lat', None)
        lng = self.request.query_params.get('lng', None)
        if lat and lng:
            return _check_polygon(queryset, float(lng), float(lat))

        return queryset


class ServiceAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Class ServiceAreaDetail - views - Django DRF - Mozio Challenge
    provides Service Area object update, deletion and object overview
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    filter_fields = ['name','price','provider']


def _check_polygon(queryset, lng, lat):
    point = Point(lng, lat)
    queryset_filtered = []

    for queryset_object in queryset:
        try:
            queryset_object_area = loads(queryset_object.area)
            polygon = shape(queryset_object_area['geometry'])
            if polygon.contains(point):
                queryset_filtered.append(queryset_object)
        except:
            pass

    return queryset_filtered
