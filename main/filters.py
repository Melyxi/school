from django_filters import rest_framework as filters
from .models import Education_1, Districts


class EducationFilter(filters.FilterSet):
    study_year = filters.CharFilter(lookup_expr='contains')
    district_id__district_name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Education_1
        fields = ['study_year', 'district_id__district_name']


class DistrictsFilter(filters.FilterSet):
    district_name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Districts
        fields = ['district_name']
