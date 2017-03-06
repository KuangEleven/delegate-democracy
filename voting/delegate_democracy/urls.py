from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^helloworld$', views.hello_world, name='hello world'),
    url(r'^$', views.voting_body, name='voting body'),
    url(r'^voting_body/(?P<voting_body_id>[0-9]+)/$', views.voting_body_detail, name='voting body detail')
]