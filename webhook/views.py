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
    file_location = os.listdir('./asset/data.json')
    
    with open(file_location, 'w') as json_file:
        json.dump(data, json_file)
    # print(json_dump)
    file = open(file_location, 'r')
    print("FROM FILE" + file.read())


    response = HttpResponse(json_dump, content_type='text/csv')
    #print(response)
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    return response
    return HttpResponse(status=200)





