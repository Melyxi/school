from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from main.views import DistrictsView, EducationView, EducationDetailView

router = DefaultRouter()
router.register('districts', DistrictsView)
router.register('education', EducationView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('api/', include(router.urls)),
    path('api/coordinate/<int:pk>/', EducationDetailView.as_view())

]
