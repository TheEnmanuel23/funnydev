from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
 	url(r'^grappelli/', include('grappelli.urls')), # grappelli 
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', TemplateView.as_view(template_name="home.html"), name="home"),   
    url(r'^funnydev/', include('posts.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)