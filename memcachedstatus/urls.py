from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^cache/$', 'memcachedstatus.views.cache_status', {}, name="memcachedstatus_cache"),
)