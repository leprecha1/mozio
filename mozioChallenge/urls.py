from django.contrib import admin
from django.urls import path, include

from core import views as core_views

urlpatterns = [
    path('providers/', core_views.ProviderList.as_view(), name='provider-list'),
    path('provider/<pk>', core_views.ProviderDetail.as_view(), name='provider-detail'),
    path('service_areas/', core_views.ServiceAreaList.as_view(), name='service-area-list'),
    path('service_area/<pk>', core_views.ServiceAreaDetail.as_view(), name='service-area-detail'),
    path('admin/', admin.site.urls),
]
