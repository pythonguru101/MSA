import math
import linux_metrics as lm

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
    - "procs_running"=<int_value>
    - "cpu_utilization"=<float_value>
    - "disk_busy"=<string_value>
    - "disk_reads"=<string_value>
    - "disk_writes"=<string_value>
    - "memory_used"=<string_value>
    - "memory_total"=<string_value>
    - "network_bits_received"=<string_value>
    - "network_bits_sent"=<string_value>
    """
    authentication_classes = [OAuth2Authentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        # cpu
        procs_running = lm.cpu_stat.procs_running()
        cpu_pcts = lm.cpu_stat.cpu_percents(sample_duration=1)
        cpu_utilization = 100 - cpu_pcts['idle']

        # disk
        disk_busy = lm.disk_stat.disk_busy('sda', sample_duration=1)
        disk_reads, disk_writes = lm.disk_stat.disk_reads_writes('sda1')

        # memory
        used, total, _, _, _, _ = lm.mem_stat.mem_stats()

        # network
        # rx_bits, tx_bits = lm.net_stat.rx_tx_bits('enp4s0')

        return Response(OrderedDict([
            ("procs_running", procs_running),
            ("cpu_utilization", cpu_utilization),
            ("disk_busy", disk_busy),
            ("disk_reads", disk_reads),
            ("disk_writes", disk_writes),
            ("memory_used", used),
            ("memory_total", total),
            ("network_bits_received", ""),
            ("network_bits_sent", ""),
        ])
        )
