# dating_app/utils.py
import random
import string
import requests
from django.conf import settings


def generate_otp():
    # Generate a 6-digit OTP (numeric)
    otp = ''.join(random.choices(string.digits, k=6))
    return otp

def sent_otp_to_phone(phone_number, otp):
    try:
        url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone_number}/{otp}'
        # url='http://2factor.in/API/V1/a95ec5e4-eb03-11ed-addf-0200cd936042/SMS/+919561732684/4499'
        requests.get(url)
    except Exception as e:
        return None    
