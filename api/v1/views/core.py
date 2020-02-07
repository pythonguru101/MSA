import math
from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from collections import OrderedDict
from scipy import stats as s
from objdict import ObjDict

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, OAuth2Authentication


class SystemInfoView(APIView):
    """
    SystemInfo response should be
    - "average_distance"=<int_value>
    - "club_accuracy"=<int_value>
    - "aim_tendency"=<string_value>
    - "distance_tendency"=<string_value>
    - "most_common_miss_hit"=<string_value>
    """
    authentication_classes = [OAuth2Authentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        return Response(OrderedDict([
            ("average_distance", 0),
            ("club_accuracy", 1),
            ("aim_tendency", 2),
            ("distance_tendency", 3),
            ("most_common_miss_hit", 4)
        ])
        )
