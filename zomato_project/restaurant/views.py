from django.shortcuts import render, redirect
from .models import *
from .forms import DishForm

# Create your views here.

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request,'dish_list.html',{'dishes':dishes})

def add_dish(request):
    if(request.method=="POST"):
        form = DishForm(request.POST)
        if form.is_valid :
            form.save()
            return redirect('dish_list')
        
    else : form=DishForm()

    context={'form':form}

    return render(request,'add_dish.html',context)

def create_order(request):
      if request.method=="POST":
          customer_name=request.POST.get('customer_name')
          dish_ids=request.POST.getlist('dish_ids')  

          order=Order.objects.create(customer_name=customer_name,status='received')

          selected_dishes=Dish.objects.filter(pk__in=dish_ids) 
          order.dishes.set(selected_dishes)

          return render(request, 'order_confirmation.html', {'order': order})
      dishes = Dish.objects.all()
      context = {'dishes': dishes}
      return render(request, 'create_order.html', context)


    