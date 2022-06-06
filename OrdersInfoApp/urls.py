from django.urls import path
from .views import RestaurantView, IndexView, DeliverooView, StuartView, RestaurantListView, DeliverooOrdersView, DeliverooRestOrdersCountView, StuartListView

urlpatterns = [
    # Dashboard Index
    path('', IndexView.as_view(), name='index'),
    
    # Restaurants endpoints
    path('restaurant/', RestaurantView.as_view(), name='restaurant'),
    path('restaurant-list/', RestaurantListView.as_view(), name='restaurant-list'),
    
    # Deliveroo endpoints
    path('deliveroo/', DeliverooView.as_view(), name='deliveroo'),
    path('deliveroo-list/', DeliverooOrdersView.as_view(), name='deliveroo-list'),
    path('deliveroo-restaurants/', DeliverooRestOrdersCountView.as_view(), name='deliveroo-restaurants'),
    
    # Stuart endpoints
    path('stuart/', StuartView.as_view(), name='stuart'),
    path('stuart-list/', StuartListView.as_view(), name='stuart-list'),
]
