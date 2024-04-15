from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.http import request
from cart.forms import CartAddProductForm
from .serializers import ProductSerializer,CategorySerializer
from rest_framework import viewsets, mixins

# create viewset for the serializer

class ProductViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
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
    


class CategoryViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
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
def product_list(request, category_slug=None):
    category =None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category, 'categories': categories,
                                                       'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

