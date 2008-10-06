from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^$', 'memcachedstatus.views.cache_status', {}, name="memcachedstatus_cache"),
)