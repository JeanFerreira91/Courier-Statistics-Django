from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Restaurants"

class DeliverooOrders(models.Model):
    rest_name = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    start_time = models.DateTimeField(blank=False)
    finish_time = models.DateTimeField(blank=False)
    order_number = models.IntegerField(max_length=4, blank=False)
    order_fee = models.FloatField(blank=False)
    order_tip = models.FloatField(blank=False)
    order_total = models.FloatField(blank=False)
    
    def __str__(self):
        return self.rest_name.name
    
    class Meta:
        verbose_name_plural = "Deliveroo Orders"
    
class StuartOrders(models.Model):
    rest_name = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order_time = models.DateTimeField(blank=False)
    order_number = models.IntegerField(max_length=4, blank=False)
    order_fee = models.FloatField(blank=False)
    order_multiplier = models.FloatField(blank=False)
    order_total = models.FloatField(blank=False)
    
    def __str__(self):
        return self.rest_name.name
    
    class Meta:
        verbose_name_plural = "Stuart Orders"
