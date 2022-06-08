from django.db import models
from django.db.models import Sum, Count, Avg

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a restaurant name (e.g. 'PizzaHut')",
        blank=False
        )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Restaurants"
        ordering = ['-name']


class DeliverooOrders(models.Model):
    rest_name = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        help_text="Select a Restaurant",
        blank=False
        )
    start_time = models.DateTimeField(
        help_text="Enter the start time of the order"
        )
    finish_time = models.DateTimeField(
        help_text="Enter the finish time of the order"
        )
    order_number = models.IntegerField(
        default=0000,
        help_text="Enter the order number"
        )
    order_fee = models.FloatField(
        blank=False,
        help_text="Enter the order fee (e.g. '3.15')"
        )
    order_tip = models.FloatField(
        blank=False,
        help_text="Enter the order tip (e.g. '1.00')"
        )
    
    def __str__(self):
        return self.rest_name.name
    
    # To get the total of a Deliveroo Order (order_fee + order_tip)
    def order_total(self):
        return self.order_fee + self.order_tip
    
    # To get the time spent on each Deliveroo order (finish_time - start_time)
    def time_spent(self):
        return self.finish_time - self.start_time
    
    # To calculate the total of orders per restaurant
    def orders_per_restaurant(self):
        return self.objects.filter(rest_name=self.rest_name).count()
    
    def promedy_waiting_time_minutes(self):
        return self.time_spent().total_seconds() / 60
    
    # To get the day of the order as DD/MM/YYYY
    def order_date(self):
        return self.start_time.strftime("%d/%m/%Y")
    
    # To get the names of all Deliveroo Restaurants.
    def get_restaurants(self):
        return DeliverooOrders.objects.filter(rest_name=self.rest_name).distinct()
    
    class Meta:
        verbose_name_plural = "Deliveroo Orders"
        ordering = ['-rest_name']

    
class StuartOrders(models.Model):
    rest_name = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        help_text="Select a Restaurant",
        blank=False
        )
    order_time = models.DateTimeField(
        blank=True,
        help_text="Enter the order time"
        )
    order_number = models.IntegerField(
        blank=True,
        help_text="Enter the order number (last 4 digits)"
        )
    order_fee = models.FloatField(
        blank=False,
        help_text="Enter the order fee (e.g. '4.50')"
        )
    order_multiplier = models.FloatField(
        blank=False,
        help_text="Enter the order multiplier (e.g. '2.10')"
        )
    
    def __str__(self):
        return self.rest_name.name
    
    def order_total(self):
        return self.order_fee + self.order_multiplier
    
    class Meta:
        verbose_name_plural = "Stuart Orders"
