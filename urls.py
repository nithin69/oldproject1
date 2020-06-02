from django.conf.urls import include, url, patterns
from django.contrib import admin
from ams import views, models
from django.conf import settings



urlpatterns = [
    # Examples:
    # url(r'^$', 'ambedkar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
     url(r'^', include('ams.urls')),
     url(r'^booking/', include('booking.urls')),
     url(r'^ampackers/', include('ampackers.urls')),
     url(r'^media/(?P<path>.*)/$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]

if settings.DEBUG:
        urlpatterns += patterns('',
                 (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
            )

        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)/$',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )

