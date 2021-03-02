from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Data
from .serializers import DataSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response




@csrf_exempt
@require_POST
def webhooks(request):
    jsondata = request.body
    data = json.loads(jsondata)
    json_dump = json.dumps(data)

    response = HttpResponse(json_dump, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="data.json"'

    return HttpResponse(status=200)





