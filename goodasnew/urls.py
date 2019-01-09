from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name='homepage'),
  path('sale', views.sale, name='sale'),
  path('purchase', views.purchase, name='purchase'),
]
