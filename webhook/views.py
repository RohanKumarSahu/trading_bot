from django.shortcuts import render
import os
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Data
from .serializers import DataSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home(request):
    return render(request, "index.html")


@csrf_exempt
@require_POST
def webhooks(request):
    jsondata = request.body
    data = json.loads(jsondata)

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)
        
    response = HttpResponse(data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
    print(data)
    return response

   




