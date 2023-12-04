# from django.urls import path
# from .views import UserProfileListView, UserProfileDetailView

# urlpatterns = [
#     path('userprofiles/', UserProfileListView.as_view(), name='userprofile-list'),
#     path('userprofiles/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
# ]


# dating_app urls.py
from django.urls import path,include
from .views import MobileNumberOTPView, ValidateOTPView, GoogleLoginView, LocationEnablerView,  SubscriptionDataView, UserProfileListView, GoogleLoginCompleteView 

urlpatterns = [
    path('userprofiles/', UserProfileListView.as_view(), name='userprofile-list'),   
    path('mobile-number-otp/', MobileNumberOTPView.as_view(), name='mobile-number-otp'),
    path('validate-otp/', ValidateOTPView.as_view(), name='validate-otp'),
    path('google-login/', GoogleLoginView.as_view(), name='google-login'),
    path('google-login-complete/', GoogleLoginCompleteView.as_view(), name='google-login-complete'),
    path('location-enabler/', LocationEnablerView.as_view(), name='location-enabler'),
    path('subscription-data/', SubscriptionDataView.as_view(), name='subscription-data'),
    # Add other URLs as needed
    
]
