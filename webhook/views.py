from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def webhooks(request):
    jsondata = request.body
    data = json.loads(jsondata)

return HttpResponse(status=200)