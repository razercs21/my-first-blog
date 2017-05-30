from django.conf.urls import url

from .views import (
	FutbolistaList,
	FutbolistaDetail,
	FutbolistaCreation,
	FutbolistaUpdate,
	FutbolistaDelete
)

urlpatterns = [
	
	url(r'^$', FutbolistaList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', FutbolistaDetail.as_view(), name='detail'),
	url(r'^nuevo$', FutbolistaCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', FutbolistaUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', FutbolistaDelete.as_view(), name='delete'),
    
]