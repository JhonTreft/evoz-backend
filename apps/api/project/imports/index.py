import os
from apps.helpers.status_code.index import *
from django.http import JsonResponse,StreamingHttpResponse
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from apps.helpers.src_structure.index import *
import json
import subprocess
import shutil