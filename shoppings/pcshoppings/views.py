from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Category,item





def  test_pc_shoppings(request):
    pc_shoppings_list_queryset = item.objects.all()
    return render(request,"pc_shoppings_list.html",{'pc_shoppings_list': pc_shoppings_list_queryset })


    #return
    #return HttpResponse(datetime.now())
   # return render(request, 'hello_world.html', {
        #'current_time': str(datetime.now()),
    #})



def pc_shoppings_list_view(request):
    pc_shoppings_list_queryset =item.objects.all()
   # if category:
        #pc_shoppings_list_queryset = pc_shoppings_list_queryset.filter(category=category)
    #pc_shoppings_list_queryset
    return render(request,"a1/pc_shoppings_list2.html",{'pc_shoppings_list': pc_shoppings_list_queryset })
#'category': Category.objects.all()



# Create your views here.
