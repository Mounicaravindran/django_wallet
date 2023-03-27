from django.urls import include, path
from rest_framework import routers
from wallet_app.views import WalletViewSet

router = routers.DefaultRouter()
router.register(r'wallet', WalletViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


