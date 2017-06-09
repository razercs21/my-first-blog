from django.conf.urls import url

from .views import (
    ControlList,
)

urlpatterns = [

    url(r'^$', ControlList.as_view(), name='list'),

]