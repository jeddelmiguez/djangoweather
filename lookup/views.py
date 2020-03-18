# This is my views.py file
from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=C6F3C94C-EEB0-4D9A-9D9A-EBA51FD8EDFB")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
