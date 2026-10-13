import os
import requests
from django.shortcuts import render
from .models import SearchHistory

API_KEY = os.environ.get("OPENWEATHER_API_KEY", "")

def index(request):
    weather = None
    error = None
    recent_searches = SearchHistory.objects.order_by("-searched_at")[:5]

    if request.method == "POST":
        city = request.POST.get("city", "").strip()
        if not city:
            error = "Please enter a city name."
        elif not API_KEY:
            error = "Weather API key is not configured. Set OPENWEATHER_API_KEY and restart the server."
        else:
            url = "https://api.openweathermap.org/data/2.5/weather"
            try:
                resp = requests.get(
                    url,
                    params={"q": city, "appid": API_KEY, "units": "metric"},
                    timeout=5,
                )
                data = resp.json()

                if resp.status_code == 200:
                    weather = {
                        "city": f"{data['name']}, {data['sys']['country']}",
                        "temperature": data["main"]["temp"],
                        "humidity": data["main"]["humidity"],
                        "pressure": data["main"]["pressure"],
                        "description": data["weather"][0]["description"].title(),
                        "icon": data["weather"][0]["icon"],
                    }
                    SearchHistory.objects.create(
                        city_name=data["name"],
                        temperature=data["main"]["temp"],
                        humidity=data["main"]["humidity"],
                        pressure=data["main"]["pressure"],
                        description=data["weather"][0]["description"].title(),
                    )
                    recent_searches = SearchHistory.objects.order_by("-searched_at")[:5]
                else:
                    error = data.get("message", "Could not fetch weather data.").capitalize()
            except (requests.RequestException, ValueError):
                error = "Network error. Please try again."

    return render(request, "main/index.html", {
        "weather": weather,
        "error": error,
        "recent_searches": recent_searches,
    })
