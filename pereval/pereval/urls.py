"""pereval URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from camp.views import TouristsViewset, LevelViewset, CoordsViewset, ImageViewset, PerevalViewset
from .swagger import schema_view

router = DefaultRouter()
router.register(r'tourists', TouristsViewset, basename='tourists')
router.register(r'coords', CoordsViewset, basename='coords')
router.register(r'levels', LevelViewset, basename='levels')
router.register(r'images', ImageViewset, basename='images')
router.register(r'perevals', PerevalViewset, basename='perevals')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
