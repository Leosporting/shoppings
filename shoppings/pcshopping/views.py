from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Category,item





def  test_pc_shoppings(request):
    return HttpResponse(datetime.now())
   # return render(request, 'hello_world.html', {
        #'current_time': str(datetime.now()),
    #})



def pc_shoppings_list_view(request, category=None):
    pc_shoppings_list_queryset =item.objects.all()
    if category:
        pc_shoppings_list_queryset = pc_shoppings_list_queryset.filter(category=category)
    return render("shoppings/pc_shoppings_list.html",{'pc_shoppings_list': pc_shoppings_list_queryset,'category': category.objects.all() })



# Create your views here.
