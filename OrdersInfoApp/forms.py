from dataclasses import fields
from django import forms
from django.forms import ModelForm, DateField
from .models import Restaurant, DeliverooOrders, StuartOrders

class RestaurantForm(ModelForm):
    class Meta:        
        model = Restaurant
        fields = "__all__"

class DeliverooOrdersForm(ModelForm):
    class Meta:
        model = DeliverooOrders
        fields = "__all__"

class StuartOrdersForm(ModelForm):
    class Meta:
        model = StuartOrders
        fields = "__all__"
