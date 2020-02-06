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


class ClubInfoView(APIView):
    """
    ClubInfo response should be
    - "average_distance"=<int_value>
    - "club_accuracy"=<int_value>
    - "aim_tendency"=<string_value>
    - "distance_tendency"=<string_value>
    - "most_common_miss_hit"=<string_value>
    """
    authentication_classes = [OAuth2Authentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        practice = []
        if practice is None:
            return Response({'error': 'Invalid Club ID'}, status=status.HTTP_400_BAD_REQUEST)

        # calculate average_distance, club_accuracy, aim_tendency, distance_tendency
        distance_sum = 0
        total_count = 0
        hit_count = 0
        aim_result_list = []
        distance_result_list = []
        total_miss_list = []

        for item in practice:
            if item.practice.user == request.user:
                total_count += 1
                distance_sum += item.distance
                aim_result_list.append(item.aim_result)
                distance_result_list.append(item.distance_result)

                if item.miss_hit_result:
                    total_miss_list += item.miss_hit_result

                if item.hit == 1:
                    hit_count += 1
        # print("ccc", mode(total_miss_list))

        if len(total_miss_list) > 0:
            most_common_miss_hit = s.mode(total_miss_list)[0][0]
        else:
            most_common_miss_hit = ''

        if total_count == 0:
            average_distance = 0
            club_accuracy = 0
        else:
            average_distance = math.floor(distance_sum / total_count)
            club_accuracy = math.floor(100 * hit_count / total_count)

        if len(aim_result_list) > 0:
            aim_tendency = s.mode(aim_result_list)[0][0]
        else:
            aim_tendency = ''

        if len(distance_result_list) > 0:
            distance_tendency = s.mode(distance_result_list)[0][0]
        else:
            distance_tendency = ''

        return Response(OrderedDict([
            ("average_distance", average_distance),
            ("club_accuracy", club_accuracy),
            ("aim_tendency", aim_tendency),
            ("distance_tendency", distance_tendency),
            ("most_common_miss_hit", most_common_miss_hit)
        ])
        )
