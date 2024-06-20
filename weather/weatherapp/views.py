from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Access environment variables
api = os.environ.get('API')


from .forms import CityForm
from .models import City


def home(request):
    form = CityForm(request.POST or None)
    cities = City.objects.all().order_by('-created_at','name')
    cities_info = []
    for city in cities:
        weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={city.lat}&lon={city.lon}&units=metric&appid={api}"
        res = requests.get(weather_url).json()
        temp = res["current"]["temp"]
        description = res["current"]["weather"][0]["description"]
        icon = res["current"]["weather"][0]["icon"]
        city_name = city.name
        city_id = city.id
        city_info = {
            "city_id":city_id,
            "name": city_name, 
            "temp":temp, 
            "description": description, 
            "icon": icon, 
            }
        cities_info.append(city_info)
    try:
        if request.method == "POST":
            city_name = request.POST["name"]
            city = form.save(commit=False)
            lat_lon_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api}"
            res = requests.get(lat_lon_url).json()
            city.name = res[0]["name"]
            city.lat = res[0]["lat"]
            city.lon = res[0]["lon"]
            form.save()
            messages.success(request, "City Added Successfully..")
            return redirect("home")
    except:
        messages.success(request, "Something Went Wrong, Please Try Again..")
        return redirect("home")

    return render(request, "home.html", {"form": form, "cities_info":cities_info})

def delete_city(request, pk):
    city = get_object_or_404(City, pk=pk)
    city.delete()
    messages.success(request, "Cities Updated..")
    return redirect("home")
  

