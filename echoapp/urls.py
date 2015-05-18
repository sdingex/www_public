__author__ = 'Think'
from django.conf.urls import include, url
import views



urlpatterns = [
    # Examples:
    # url(r'^$', 'www_public.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^img/',              views.img.as_view()),
    url(r'^$',                 views.index.as_view()),
]
