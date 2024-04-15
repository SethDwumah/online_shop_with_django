from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .serializers import OrderSerializer,OrderItemSerializer
from rest_framework import mixins,viewsets
from .models import Order,OrderItem



class OrderViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = Order.objects.all()
    serializer_class= OrderSerializer
    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
        
    def post(self,request):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.delete(request,id)
    

class OrderItemViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = OrderItem.objects.all()
    serializer_class= OrderItemSerializer
    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
        
    def post(self,request):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.delete(request,id)



# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()

        return render(request, 'orders/order/created.html',{'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart':cart,'form':form})

