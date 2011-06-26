from django.conf.urls.defaults import *
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', 'blog.views.home'),
	url(r'^list/(\d+)?$', 'blog.views.blog_list'),
	url(r'^(detail|info)/(?P<id>\d+)/((?P<showComments>.*)/)?$'
, 'blog.views.blog_detail'),

	url(r'^search/(\w+)*$', 'blog.views.blog_search'),
	url(r'^editcomment/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.comment_edit'),
	
)
	
