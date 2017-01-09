from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Category,item
from django.views.generic import ListView, DetailView
import copy



class Item_list_view(ListView):
    model=item



    #def categories(self):
        #return Category.objects.all()

    #def get_queryset(self):
        #query_set = super(Item_list_view, self).get_queryset()
        #self.kwargs=kwargs
        #self.kwargs.get('category')
        #category = self.kwargs.get('category')
        #category=1

        #if category:
           # query_set = query_set.filter(category=category)
       # return query_set


item_list_view=Item_list_view.as_view()




def  home(request):
    return  render(request,'index.html')


def  test_pc_shoppings(request):
    pc_shoppings_list_queryset = item.objects.all()
    return render(request,"pc_shoppings_list.html",{'pc_shoppings_list': pc_shoppings_list_queryset })


    #return
    #return HttpResponse(datetime.now())
   # return render(request, 'hello_world.html', {
        #'current_time': str(datetime.now()),
    #})



def pc_shoppings_list_view(request,category=None):
    pc_shoppings_list_queryset =item.objects.all()
    all_category=copy.copy(Category.objects.all())


    if category:

            category_id=Category.objects.all().filter(name=category)
            if category_id:
                pc_shoppings_list_queryset = pc_shoppings_list_queryset.filter(category=category_id)
            else:
                error_message=('ERROR!!   category:{0}  does not  exist!! \n it must be in {1} '.format(category,all_category))
                return render(request, "shoppings_list.html",
                              { 'error_message': error_message})




    return render(request, "shoppings_list.html",
                  {'pc_shoppings_list': pc_shoppings_list_queryset, 'categories': Category.objects.all()})
    #pc_shoppings_list_queryset

#'category': Category.objects.all()



# Create your views here.
