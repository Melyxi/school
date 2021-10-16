from rest_framework import serializers

from main.models import Districts, Education_1


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    district_id = DistrictSerializer(read_only=True)

    class Meta:
        model = Education_1
        fields = '__all__'


class RetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education_1
        fields = ('id', 'school_long', 'school_lat')
