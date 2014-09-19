from django.conf.urls.defaults import *
from SpeakBinary.views import speakBinary
from django.conf import settings as cfg
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    url(r'^$', speakBinary, name='speakBinary'),
    # (r'^binary/', include('binary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
print  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')
if cfg.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media'), "show_indexes":True}, ))

