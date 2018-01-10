from django.conf.urls import url
from rcapp import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^recordings/$', views.RecordingList),
    url(r'^recordings/(?P<pk>[0-9]+)/$', views.RecordingDetail),
    url(r'^users/$', views.UserList),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail),
]
