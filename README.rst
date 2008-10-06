===================================================
A memcached status app for the django web-framework
===================================================

This app provides one simple view ready for integration into the admin
interface. The view will - together with the default template - output the
status of the configured `memcache-daemon`_.

INSTALLATION
------------

Put the 'memcachedstatus' folder on your Python-Path, add 'memcachedstatus' to
settings.INSTALLED_APPS and add an entry to your url-conf like the following:

    url(r'^admin/memcached/', include('memcachedstatus.urls'))
    
.. _`memcache-daemon` : http://danga.com/memcached/