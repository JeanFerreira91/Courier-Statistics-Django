from django.urls import path
from .views import RestaurantView, IndexView, DeliverooView, StuartView, RestaurantListView, DeliverooListView, StuartListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('restaurant/', RestaurantView.as_view(), name='restaurant'),
    path('restaurant-list/', RestaurantListView.as_view(), name='restaurant-list'),
    path('deliveroo/', DeliverooView.as_view(), name='deliveroo'),
    path('deliveroo-list/', DeliverooListView.as_view(), name='deliveroo-list'),
    path('stuart/', StuartView.as_view(), name='stuart'),
    path('stuart-list/', StuartListView.as_view(), name='stuart-list'),
]
