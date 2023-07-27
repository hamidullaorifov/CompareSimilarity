from django.urls import path,include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from . import views


router = routers.DefaultRouter()

router.register('',views.UserApiViewSet,basename='users')

urlpatterns = [
    path('login/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('',include(router.urls)),
]