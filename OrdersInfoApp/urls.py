from django.urls import path
from .views import RestaurantView, IndexView, DeliverooView, StuartView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('restaurant/', RestaurantView.as_view(), name='restaurant'),
    path('deliveroo/', DeliverooView.as_view(), name='deliveroo'),
    path('stuart/', StuartView.as_view(), name='stuart'),
]
