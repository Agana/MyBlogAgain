from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    #(r'^admin/', include(admin.site.urls)),
    (r'^polls/', include('polls.urls')),
    (r'^notes/', include('notes.urls')),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
    
)
