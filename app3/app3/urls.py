from django.conf.urls import url
from .views import homev,aboutv,contactv
urlpatterns = [
    url(r'^$',homev,name='homel'),
    url(r'^about/$',aboutv,name='aboutl'),
    url(r'^contact$',contactv,name='contactl'),
]
