from dataclasses import fields
from django import forms
from django.forms import ModelForm, DateField
from .models import Restaurant, DeliverooOrders, StuartOrders
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset
from crispy_forms.bootstrap import StrictButton, FormActions

class RestaurantForm(ModelForm):
    class Meta:        
        model = Restaurant
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            FormActions(
                Submit('save', 'Save New Restaurant', css_class='btn-primary'),
            )
        )
        self.helper.form_id = 'id-restaurantForm'
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-4'


class DeliverooOrdersForm(ModelForm):
    start_time = forms.DateTimeField(
        label='Start Time',
        widget=forms.widgets.DateInput(attrs={'type': 'datetime-local'}),
    )
    finish_time = forms.DateTimeField(
        label='Finish Time',
        widget=forms.widgets.DateInput(attrs={'type': 'datetime-local'}),
    )
    
    class Meta:
        model = DeliverooOrders
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'rest_name',
            'start_time',
            'finish_time',
            'order_number',
            'order_fee',
            'order_tip',
            FormActions(
                Submit('save', 'Save New Order', css_class='btn-primary'),
            )
        )
        self.helper.form_id = 'id-deliverooOrdersForm'
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-4'
        self.fields['start_time'].required = False
        self.fields['finish_time'].required = False
        self.fields['order_number'].required = False


class StuartOrdersForm(ModelForm):
    order_time = forms.DateTimeField(
        label='Start Time',
        widget=forms.widgets.DateInput(attrs={'type': 'datetime-local'}),
    )
    
    class Meta:
        model = StuartOrders
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'rest_name',
            'order_time',
            'order_number',
            'order_fee',
            'order_multiplier',
            FormActions(
                Submit('save', 'Save New Order', css_class='btn-primary'),
            )
        )
        self.helper.form_id = 'id-stuartOrdersForm'
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-4'
        self.fields['order_time'].required = False
        

