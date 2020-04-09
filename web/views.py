from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json
# Create your views here.
def Login(request):
    if request.method == 'POST':
        result = {}
        username = request.POST.get('username')
        password = request.POST.get('password')

        result['user'] = username
        result['paw'] = password

        result = json.dumps(result)
        return HttpResponse(result)
    else:
        return render_to_response('login.html')

