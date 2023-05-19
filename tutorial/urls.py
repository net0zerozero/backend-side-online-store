from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from quickstart import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/register/', views.RegisterView.as_view(), name="sign_up"),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/wishlist/', views.WishListView.as_view(), name='wishlist'),
    path('api/wishlist/<int:product_id>/', views.WishListView.as_view()),
    path('api/cart/', views.CartView.as_view(), name='cart'),
    path('api/cart/<int:product_id>/', views.CartView.as_view()),
    path('api/user/', views.UserView.as_view(), name='user'),  # Добавлен новый путь для получения информации о пользователе
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)