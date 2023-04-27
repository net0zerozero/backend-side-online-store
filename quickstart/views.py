from django.forms import ValidationError
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product, WishList
from .serializers import CategorySerializer, ProductSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact'],
        'title': ['exact']
    }


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = {
        'id': ['exact'],
        'price': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'title': ['exact'],
        'category': ['exact']
    }
    ordering_fields = ['title', 'price']
    ordering = ['title']
    search_fields = ['title']

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class WishListView(APIView):       
    def get(self, request):
        wish_list = WishList.objects.filter(user=self.request.user.id).values_list('product', flat=True)
        return Response(wish_list)

    def post(self, request):
        product_id = request.data.get('product_id')
        if not product_id:
            raise ValidationError('Product id is required')
        
        if not WishList.objects.filter(user=self.request.user).exists():
            # wish_list = WishList.objects.create(user=self.request.user, product=[product_id])
            # wish_list with user and product
            wish_list = WishList.objects.create(user=self.request.user)
            wish_list.product.add(product_id)
        else:
            wish_list = WishList.objects.get(user=self.request.user)
            wish_list.product.add(product_id)
        return Response({'status': 'success'})

    def delete(self, request):
        product_id = request.data.get('product_id')
        if not product_id:
            raise ValidationError('Product id is required')
        wish_list = WishList.objects.get(user=self.request.user)
        wish_list.product.remove(product_id)
        return Response({'status': 'success'})
