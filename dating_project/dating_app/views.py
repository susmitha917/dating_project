import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import requests

from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileListView(View):
    def get(self, request, *args, **kwargs):
        user_profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(user_profiles, many=True)
        return JsonResponse(serializer.data, safe=False)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# class UserProfileDetailView(View):
#     def get(self, request, pk, *args, **kwargs):
#         user_profile = UserProfile.objects.get(pk=pk)
#         serializer = UserProfileSerializer(user_profile)
#         return JsonResponse(serializer.data)

#     @method_decorator(csrf_exempt)
#     def put(self, request, pk, *args, **kwargs):
#         user_profile = UserProfile.objects.get(pk=pk)
#         data = json.loads(request.body)
#         serializer = UserProfileSerializer(user_profile, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     def delete(self, request, pk, *args, **kwargs):
#         user_profile = UserProfile.objects.get(pk=pk)
#         user_profile.delete()
#         return JsonResponse({'message': 'User profile deleted successfully'}, status=204)

# dating_app/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from .models import UserProfile
from .utils import generate_otp, sent_otp_to_phone
from social_django.utils import psa 
from social_django.views import complete
from django.views.decorators.http import require_GET 
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login




@method_decorator(csrf_exempt, name='dispatch')
class MobileNumberOTPView(View):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        mobile_number = data.get('mobile_number')
        try:
            user_profile = UserProfile.objects.get(mobile_number=mobile_number)
            otp = generate_otp()
            sent_otp_to_phone(mobile_number,otp)
            user_profile.otp = otp
            user_profile.save()
            return JsonResponse({'detail': 'OTP sent successfully'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'detail': 'User not found'}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class ValidateOTPView(View):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        mobile_number = data.get('mobile_number')
        entered_otp = data.get('entered_otp')
        try:
            user_profile = UserProfile.objects.get(mobile_number=mobile_number)
            if user_profile.otp == entered_otp:
                user_profile.is_otp_verified = True
                user_profile.save()
                return JsonResponse({'detail': 'OTP verified successfully'}, status=200)
            else:
                return JsonResponse({'detail': 'Invalid OTP'}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'detail': 'User not found'}, status=404)
        
@method_decorator(csrf_exempt, name='dispatch')
class GoogleLoginView(View):
    def get(self, request, *args, **kwargs):
        return redirect('social:begin', 'google-oauth2')
    
@method_decorator(csrf_exempt, name='dispatch')
class GoogleLoginCompleteView(View):
    def get(self, request, *args, **kwargs):
        # response = complete(request, backend='google-oauth2')

        if request.user.is_authenticated:
            # User is authenticated, perform authenticated user actions
            return HttpResponse("Google authentication successful. You are logged in!")

        # User is not authenticated, perform actions for non-authenticated users
        return HttpResponse("Google authentication successful, but you are not logged in.")
        
@method_decorator(csrf_exempt, name='dispatch')
class LocationEnablerView(View):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        longitude = data.get('longitude')
        latitude = data.get('latitude')
        # Implement location enabler logic here
        if latitude is not None and longitude is not None:
               # Make a request to Google Geocoding API
               api_key = 'AIzaSyAyDttykay0fXTbJnrMQT6SOEqqb4f5OGY'
               api_url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}'

               response = requests.get(api_url)
               data = response.json()

               # Extract relevant information from the API response
               location_info = data.get('results', [])[0] if data.get('results') else None

               if location_info:
                   formatted_address = location_info.get('formatted_address', 'N/A')
                   return JsonResponse({'formatted_address': formatted_address}, status=200)
               else:
                   return JsonResponse({'error': 'Location not found'}, status=400)
        else:
               return JsonResponse({'error': 'Latitude and longitude are required'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class SubscriptionDataView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)

            # Extract subscription data from the request
            plan_type = data.get('plan_type')

            # Get subscription details based on the plan type
            subscription_details = get_subscription_details(plan_type)

            if subscription_details:
                return JsonResponse(subscription_details, status=200)
            else:
                return JsonResponse({'error': 'Invalid plan type'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def get_subscription_details(plan_type):

    subscription_data = {
        'basic': {
            'price': 9.99,
            'benefits': ['Access to basic features', 'Limited swipes'],
            'duration': '1 month',
            'swipe_limit': 100,
        },
        'premium': {
            'price': 19.99,
            'benefits': ['Access to all features', 'Unlimited swipes'],
            'duration': '3 months',
            'swipe_limit': None, 
        },
    }

    return subscription_data.get(plan_type)