"""stock URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from app.views import home,Myregistration,profile,company_list,recent_stock

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stock/accounts/register/',Myregistration.as_view()),
    url(r'^stock/admin/', include(admin.site.urls)),
    #url(r'^stock/accounts/login/', auth_views.login),
    url(r'^stock/accounts/', include('registration.backends.simple.urls')),
    # Password URL workarounds for Django 1.6: 
    #   http://stackoverflow.com/questions/19985103/
    url(r'^stock/password/change/$',
                    auth_views.password_change,
                    name='password_change'),
    url(r'^stock/password/change/done/$',
                    auth_views.password_change_done,
                    name='password_change_done'),
    url(r'^stock/password/reset/$',
                    auth_views.password_reset,
                    name='password_reset'),
    url(r'^stock/accounts/password/reset/done/$',
                    auth_views.password_reset_done,
                    name='password_reset_done'),
    url(r'^stock/password/reset/complete/$',
                    auth_views.password_reset_complete,
                    name='password_reset_complete'),
    url(r'^stock/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                    auth_views.password_reset_confirm,
                    name='password_reset_confirm'),
    url(r'^stock/$',home, name='home'),
    url(r'stock/profile/$',profile,name='profile'),
    url(r'stock/companies/$',company_list),
    url(r'stock/viewer/(?P<sym>\d+)/$',recent_stock),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
