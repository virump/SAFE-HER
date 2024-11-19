from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Alert
from django.contrib.auth.hashers import make_password
from .models import User, Location 
# from django.core.mail import send_mail
from django.utils import timezone
# tracking/views.py



# tracking/views.py

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from twilio.rest import Client
from django.conf import settings
# tracking/views.py
def send_sms_alert(phone_numbers, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for number in phone_numbers:
        client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=number
        )


@csrf_exempt
def send_alert(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        emergency_type = data.get('emergency_type', 'Emergency')
        custom_message = data.get('custom_message', '')
        user = request.user

        if user.is_authenticated:
            # Save alert data to the database
            Alert.objects.create(
                user=user,
                latitude=latitude,
                longitude=longitude,
                emergency_type=emergency_type,
                custom_message=custom_message
            )

            # Prepare the email message
            location_url = f"https://www.google.com/maps?q={latitude},{longitude}"
            message = f"Emergency alert from {user.username}! Location: {location_url}\nType: {emergency_type}\nMessage: {custom_message}"

            # Send the email notifications
            send_mail(
                'Emergency Alert',
                message,
                'aryanthemafia79@gmail.com',
                ['pathakvirru@gmail.com'],
                fail_silently=False,
            )

            return JsonResponse({'message': 'Alert sent successfully'}, status=200)
        else:
            return JsonResponse({'error': 'User not authenticated'}, status=401)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        user = User(name=name, email=email, password=password)
        user.save()
        return redirect('alert')
    return render(request, 'register.html')

def alert(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.POST['email'])
        location = request.POST['location']
        message = request.POST['message']
        alert = Alert(user=user, location=location, message=message)
        alert.save()
        return redirect('success')
    return render(request, 'alert.html')

def success(request):
    return render(request, 'success.html')

def about(request):
    return render(request, 'about.html')

def track(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.get(email=email)
        try:
            latitude = float(request.POST['latitude'])
            longitude = float(request.POST['longitude'])
        except ValueError:
            return render(request, 'safety_app/track.html', {'error': 'Invalid latitude or longitude'})
        
        location = Location(user=user, latitude=latitude, longitude=longitude, timestamp=timezone.now())
        location.save()

         # Send Email to Family and Admin
        message = f"Help! I need assistance. My location is: Latitude: {latitude} Longitude: {longitude}"
        send_mail(
            'Emergency Alert',
            message,
            'your-email@example.com',
            ['family@example.com', 'admin@example.com']
        )
        return redirect('show_map')
    return render(request, 'safety_app/track.html')

def show_map(request):
    locations = Location.objects.all()
    return render(request, 'map.html')

# def front(request):
    # return render(request,'front.html')


# tracking/views.py
# tracking/views.py

from .utils import get_nearby_police_stations

import requests

def get_nearby_police_stations(latitude, longitude):
    api_key = 'your_google_places_api_key'
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=5000&type=police&key={api_key}"
    response = requests.get(url)
    results = response.json().get('results', [])
    return [place['name'] for place in results]

