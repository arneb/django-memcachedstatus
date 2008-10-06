import datetime, re
from django.http import Http404
from django.conf import settings
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.translation import ugettext_lazy as _



MEMCACHE = re.match("memcached://([.\w]+:\d+)", getattr(settings, 'CACHE_BACKEND', ''))




@staff_member_required
def cache_status(request):
    """
    Fetch memcache status and display it.
    Taken and modified from: http://effbot.org/zone/django-memcached-view.htm
    
    """
    try:
        import memcache
    except ImportError:
        return direct_to_template(request, 'memcachedstatus/cache_status.html', {'error': _(u'Memcached library not installed')})

    if not MEMCACHE:
        return direct_to_template(request, 'memcachedstatus/cache_status.html', {'error': _(u'No memcached configured')})

    host = memcache._Host(MEMCACHE.group(1))
    host.connect()
    host.send_cmd("stats")

    class Stats:
        pass

    stats = Stats()

    while 1:
        line = host.readline().split(None, 2)
        if line[0] == "END":
            break
        stat, key, value = line
        try:
            # convert to native type, if possible
            value = int(value)
            if key == "uptime":
                value = datetime.timedelta(seconds=value)
            elif key == "time":
                value = datetime.datetime.fromtimestamp(value)
        except ValueError:
            pass
        setattr(stats, key, value)

    host.close_socket()

    context = {'stats': stats, 
               'hit_rate': 100 * stats.get_hits / stats.cmd_get,}
               
    return direct_to_template(request, 'memcachedstatus/cache_status.html', context)



