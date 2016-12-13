from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def  test_pc_shoppings(request):
    return HttpResponse(datetime.now())
   # return render(request, 'hello_world.html', {
        #'current_time': str(datetime.now()),
    #})



# Create your views here.
