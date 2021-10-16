from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from main.filters import EducationFilter, DistrictsFilter
from main.models import Districts, Education_1
from main.serializers import DistrictSerializer, EducationSerializer, RetrieveSerializer

class IsAdminPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class DistrictsView(ModelViewSet):
    queryset = Districts.objects.all()
    serializer_class = DistrictSerializer
    filterset_class = DistrictsFilter

class EducationView(ModelViewSet):
    queryset = Education_1.objects.all()
    serializer_class = EducationSerializer
    filterset_class = EducationFilter

class EducationDetailView(RetrieveAPIView):
    permission_classes = [IsAdminPermissions]
    serializer_class = RetrieveSerializer
    queryset = Education_1.objects.all()