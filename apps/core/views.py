import datetime
import json
import logging
import pandas as pd

from collections import OrderedDict

from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse

logger = logging.getLogger(__name__)


class ReportView(TemplateView):
    template_name = 'report.html'


class HomeView(TemplateView):
    template_name = 'home.html'
