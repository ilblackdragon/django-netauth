try:
    from django.conf.urls import url, patterns
except ImportError:
    from django.conf.urls.defaults import url, patterns # Django < 1.4

from django.views.generic.base import TemplateView

from netauth import views


urlpatterns = patterns('',
    url(r'^begin/(\w+)/$', views.begin, name='netauth-begin'),
    url(r'^complete/(\w+)/$', views.complete, name='netauth-complete'),
    url(r'^extra/(\w+)/$', views.extra, name='netauth-extra'),
    url(r'^login/$', TemplateView.as_view(template_name='netauth/login.html'), name='netauth-login'),
    url(r'^logout/$', views.logout, name='netauth-logout'),

    url(r'^ya_proxy/$', TemplateView.as_view(template_name='netauth/yandex_proxy.html'), name='netauth-yandex-proxy'),
)
