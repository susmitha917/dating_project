# from django.contrib.gis.db import models

# class UserProfile(models.Model):
#     name = models.CharField(max_length=255)
#     bio = models.TextField()
#     age = models.IntegerField()
#     location = models.PointField()  # You might need to use a GeoDjango field for location
#     images = models.ImageField(upload_to='images/', null=True,blank=True)
#     distance = models.FloatField()
#     preference_gender = models.CharField(max_length=10)
#     preference_age = models.IntegerField()

# # Additional Fields
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     occupation = models.CharField(max_length=100, blank=True, null=True)
#     education = models.CharField(max_length=100, blank=True, null=True)
#     hobbies = models.TextField(blank=True, null=True)
#     relationship_status = models.CharField(max_length=20, blank=True, null=True)
#     ethnicity = models.CharField(max_length=50, blank=True, null=True)
#     height = models.FloatField(blank=True, null=True)
    
#     # Timestamps
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# dating_api/models.py
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    interests = models.CharField(max_length=255)
    images = models.ImageField(null=True,blank=True)
    distance = models.IntegerField()
    preference_gender = models.CharField(max_length=10)
    preference_age = models.IntegerField()
    mobile_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    is_otp_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    height = models.FloatField(blank=True, null=True)

    # Add other fields as needed
    
