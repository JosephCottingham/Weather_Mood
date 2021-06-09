from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from ip2geotools.databases.noncommercial import DbIpCity

from .models import (
    Mood
)

from .forms import (
    Mood_Create_Form
)

from open_weather_api.open_weather_api_client import OpenWeatherApiClient
from ipware import get_client_ip
from django.urls import reverse 

appid = '178db63aed00f6e4daaa06009b04438b'

weather_client = OpenWeatherApiClient(appid)
weather_ap_is_controller = weather_client.weather_ap_is

class Mood_View(ListView):

    template_name='mood/Mood_View.html'
    model = Mood
    
    def get_queryset(self):
        object_list = self.model.objects.order_by('created').all()
        return object_list

class Mood_CreateView(CreateView):
    
    template_name = 'mood/Mood_CreateView.html'
    model = Mood
    form_class = Mood_Create_Form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print('ip')
        self.object.ip, is_routable = get_client_ip(self.request)
        if is_routable:
            ip_data = DbIpCity.get(self.object.ip, api_key='free')        
            weather_data = weather_ap_is_controller.get_weather_by_latitude_and_longitude(lat=ip_data.latitude, lon=ip_data.longitude)
        else:
            weather_data = weather_ap_is_controller.get_weather_by_latitude_and_longitude(lat=0, lon=0)
        weather_main = weather_data.weather[0].main
        self.object.weather = weather_main
        self.object.save()
        return HttpResponseRedirect(reverse('Mood_View'))