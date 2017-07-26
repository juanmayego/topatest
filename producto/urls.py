from django.conf.urls import url

from producto import views

urlpatterns = [
  url(r'^$', views.ProductoList.as_view(), name='producto_list'),
  url(r'^new$', views.ProductoCreate.as_view(), name='producto_new'),
  url(r'^edit/(?P<pk>\d+)$', views.ProductoUpdate.as_view(), name='producto_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.ProductoDelete.as_view(), name='producto_delete'),
]