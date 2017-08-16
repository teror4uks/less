from django.conf.urls import url
from django.contrib import admin

from shorter.views import HomeView, LessBasedView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'(?P<shortcode>[\w-]+)/$', LessBasedView.as_view(), name='scode'),
]
