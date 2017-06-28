"""games URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,patterns,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from app.views import Myregistration,home,profile,gamelist_view,contact,eachgameview,platform,genre

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^games/accounts/register/',Myregistration.as_view()),
    url(r'^games/admin/', include(admin.site.urls)),
    #url(r'^games/accounts/login/', auth_views.login),
    url(r'^games/accounts/', include('registration.backends.simple.urls')),
    # Password URL workarounds for Django 1.6: 
    #   http://stackoverflow.com/questions/19985103/
    url(r'^games/password/change/$',
                    auth_views.password_change,
                    name='password_change'),
    url(r'^games/password/change/done/$',
                    auth_views.password_change_done,
                    name='password_change_done'),
    url(r'^games/password/reset/$',
                    auth_views.password_reset,
                    name='password_reset'),
    url(r'^games/accounts/password/reset/done/$',
                    auth_views.password_reset_done,
                    name='password_reset_done'),
    url(r'^games/password/reset/complete/$',
                    auth_views.password_reset_complete,
                    name='password_reset_complete'),
    url(r'^games/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                    auth_views.password_reset_confirm,
                    name='password_reset_confirm'),
    url(r'^games/$',home), 
    url(r'^games/profile/$',profile),
    url(r'^games/list/$',gamelist_view),
    url(r'^games/contact/$',contact),
    url(r'^games/(?P<gameid>\d+)/$',eachgameview),
    url(r'^games/platform/(?P<pid>\d+)/$',platform),
    url(r'^games/genre/(?P<gid>\d+)/$',genre),
]
