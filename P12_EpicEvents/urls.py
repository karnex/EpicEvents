from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_nested import routers
from django.views.generic.base import RedirectView

from authentication.views import AnonymizeViewSet
from event.views import ClientViewSet

router = routers.SimpleRouter()
router.register(r'clients', ClientViewSet, basename='clients')

urlpatterns = [
    path('admin', admin.site.urls),
    re_path(r'^$', RedirectView.as_view(url='admin')),
    path('api-auth', include('rest_framework.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/', include('authentication.urls')),
    path('api/anonymize-my-account', AnonymizeViewSet.as_view({'put': 'update'})),
    path('api/token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
