from django.urls import path
from .views.catalog import CatalogAPIView
from .views.main import MainPageAPIView


urlpatterns = [
    path('', MainPageAPIView.as_view(), name='main'),
    path('catalog/', CatalogAPIView.as_view(), name='catalog'),
] 

