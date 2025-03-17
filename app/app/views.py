from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  if request.method == 'GET':
     return render(request, 'app/index.html')
  elif request.method == 'POST':
      return HttpResponse("You've made a POST request.")
