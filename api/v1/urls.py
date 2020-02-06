from django.conf.urls import url, include

from .views import *

import oauth2_provider.views as oauth2_views

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    url(r'^authorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    url(r'^token/$', oauth2_views.TokenView.as_view(), name="token"),
    url(r'^revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

urlpatterns = [
    # club info
    url(r'^practice/club_info/(?P<club_id>[-\w]+)/$', ClubInfoView.as_view()),
    # oauth2
    url(r'^o/', include(oauth2_endpoint_views)),
]
