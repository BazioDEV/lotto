from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'thailotto', views.ResultViewSet)
router.register(r'laos-vip', views.VipResultViewSet)
router.register(r'laos-lotto', views.LottoResultViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]