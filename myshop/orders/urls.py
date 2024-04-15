from django.urls import path, include
from .views import order_create, OrderViewset, OrderItemViewset
from rest_framework.routers import DefaultRouter

app_name = 'orders'

router = DefaultRouter()
router.register('orders', OrderViewset, basename='orders')

router_orderitem = DefaultRouter()
router_orderitem.register('ordersitems', OrderItemViewset, basename='ordersitems')

urlpatterns = [
    path('create/',order_create, name='order_create'),
    path('order_api/',include(router.urls)),
    path('orders_items_api/',include(router_orderitem.urls)),
]