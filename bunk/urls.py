from django.conf.urls import url

from . import views

app_name = 'bunk'

urlpatterns = [
    url(r'^$', views.MainFeed.as_view(), name='main'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserFeed.as_view(), name='user'),
    url(r'^bunks/$', views.BunkView.as_view()),
]
