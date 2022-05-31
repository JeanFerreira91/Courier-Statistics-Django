from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import RestaurantForm, DeliverooOrdersForm, StuartOrdersForm

# Create your views here.
# def index(request):
#     # if this is a POST request we need to process the form data
#     if(request.method == 'POST'):
#         # create a form instance and populate it with data from the request:
#         form = RestaurantForm(request.POST)
#         # check whether it's valid:
#         if(form.is_valid()):
#             # process the data in form.cleaned_data as required
#             form.save()
#             # redirect to a new URL:
#             return HttpResponseRedirect('/')
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = RestaurantForm()
#     return render(request, 'OrdersInfoApp/index.html', {'form': form})

class IndexView(View):
    initial = {'key': 'value'}
    template_name = 'OrdersInfoApp/index.html'
    
    # The GET method is called when the browser is requesting a page
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class RestaurantView(View):
    form_class = RestaurantForm
    initial = {'key': 'value'}
    template_name = 'OrdersInfoApp/restaurant_form.html'
    
    # The GET method is called when the browser is requesting a page
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    # The POST method is called when the browser has finished sending data
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # process form cleaned data
            form.save()
            return HttpResponseRedirect('/restaurant/')
        return render(request, self.template_name, {'form': form})

class DeliverooView(View):
    form_class = DeliverooOrdersForm
    initial = {'key': 'value'}
    template_name = 'OrdersInfoApp/deliveroo_form.html'
    
    # The GET method is called when the browser is requesting a page
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    # The POST method is called when the browser has finished sending data
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # process form cleaned data
            form.save()
            return HttpResponseRedirect('/deliveroo/')
        return render(request, self.template_name, {'form': form})

class StuartView(View):
    form_class = StuartOrdersForm
    initial = {'key': 'value'}
    template_name = 'OrdersInfoApp/stuart_form.html'
    
    # The GET method is called when the browser is requesting a page
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    # The POST method is called when the browser has finished sending data
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # process form cleaned data
            form.save()
            return HttpResponseRedirect('/stuart/')
        return render(request, self.template_name, {'form': form})