from dataclasses import fields
from django import forms
from django.forms import ModelForm, DateField
from .models import Restaurant, DeliverooOrders, StuartOrders
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RestaurantForm(ModelForm):
    class Meta:        
        model = Restaurant
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-restaurantForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'restaurant'
        self.helper.add_input(Submit('submit', 'Submit'))

class DeliverooOrdersForm(ModelForm):
    class Meta:
        model = DeliverooOrders
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-deliverooOrdersForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'deliveroo'
        self.helper.add_input(Submit('submit', 'Submit'))

class StuartOrdersForm(ModelForm):
    class Meta:
        model = StuartOrders
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-stuartOrdersForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'stuart'
        self.helper.add_input(Submit('submit', 'Submit'))
