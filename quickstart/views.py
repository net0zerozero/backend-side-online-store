from django.forms import ValidationError
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product, WishList, Cart
from .serializers import CategorySerializer, ProductSerializer, UserSerializer, UserDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated





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
        if serializer.is_valid():
            user = serializer.save()

            # Generate tokens for the registered user
            access_token = AccessToken.for_user(user)

            # Include tokens in the response
            response_data = {
                'id': user.id,
                'email': user.email,
                'name': user.username,
                'access_token': str(access_token),
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
    


class WishListView(APIView):
    permission_classes = [IsAuthenticated]
       
    def get(self, request):
        wish_list = WishList.objects.filter(user=self.request.user.id).values_list('product', flat=True)
        return Response(wish_list)

    def post(self, request):
        product_id = request.data.get('product_id')
        if not product_id:
            return Response({'status': 'error', 'message': 'Product id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not WishList.objects.filter(user=self.request.user).exists():
            wish_list = WishList.objects.create(user=self.request.user)
            wish_list.product.add(product_id)
        else:
            wish_list = WishList.objects.get(user=self.request.user)
            wish_list.product.add(product_id)
        return Response({'status': 'success'})

    def delete(self, request, product_id=None):
        if product_id is None:
            return Response({'status': 'error', 'message': 'Product id is required'}, status=status.HTTP_400_BAD_REQUEST)
        wish_list = get_object_or_404(WishList, user=self.request.user)
        wish_list.product.remove(product_id)
        return Response({'status': 'success'})




class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        cart = Cart.objects.filter(user=self.request.user.id).values_list('product', flat=True)
        return Response(cart)

    def post(self, request):
        product_id = request.data.get('product_id')
        if not product_id:
            return Response({'status': 'error', 'message': 'Product id is required'}, status=status.HTTP_400_BAD_REQUEST)

        if not Cart.objects.filter(user=self.request.user).exists():
            cart = Cart.objects.create(user=self.request.user)
            cart.product.add(product_id)
        else:
            cart = Cart.objects.get(user=self.request.user)
            cart.product.add(product_id)
        return Response({'status': 'success'})

    def delete(self, request, product_id=None):
        if product_id is None:
            return Response({'status': 'error', 'message': 'Product id is required'}, status=status.HTTP_400_BAD_REQUEST)
        cart = get_object_or_404(Cart, user=self.request.user)
        cart.product.remove(product_id)
        return Response({'status': 'success'})
    








