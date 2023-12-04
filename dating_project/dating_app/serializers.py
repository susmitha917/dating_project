# from rest_framework import serializers
# from .models import UserProfile
# from rest_framework_gis.serializers import GeoFeatureModelSerializer

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         geo_field='location'
#         fields = '__all__'

# class UserProfileGeoSerializer(GeoFeatureModelSerializer, UserProfileSerializer):
#     pass


# dating_api/serializers.py
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
