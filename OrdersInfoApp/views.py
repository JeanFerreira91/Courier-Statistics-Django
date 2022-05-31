from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Restaurant, DeliverooOrders, StuartOrders
from .forms import RestaurantForm, DeliverooOrdersForm, StuartOrdersForm

# Create your views here.
def index(request):
    # if this is a POST request we need to process the form data
    if(request.method == 'POST'):
        # create a form instance and populate it with data from the request:
        form = RestaurantForm(request.POST)
        # check whether it's valid:
        if(form.is_valid()):
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RestaurantForm()
    return render(request, 'OrdersInfoApp/index.html', {'form': form})
