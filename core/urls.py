"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import RegisterView, ProfileView
from exchanges.views import ExchangeViewSet, ExchangeAccountViewSet
from trades.views import TradeViewSet

router = DefaultRouter()
router.register(r'exchanges/list', ExchangeViewSet, basename='exchange-list')
router.register(r'exchanges', ExchangeAccountViewSet, basename='exchange-accounts')
router.register(r'trades', TradeViewSet, basename='trades')
urlpatterns = [
    path('admin/', admin.site.urls),
    # Auth Routing Hooks
    path('api/auth/register/', RegisterView.as_view(), name='auth_register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/profile/', ProfileView.as_view(), name='auth_profile'),
    
    # Modular Features Hub
    path('api/', include(router.urls)),
]
