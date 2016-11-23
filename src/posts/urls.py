from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^$', PostList.as_view(), name='post_list'),
	url(r'entry/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<pk>\d+)-(?P<slug>[-\w]*)/$', PostDetail.as_view(), name='post_detail'),
]