from django.shortcuts import render
from django.http import HttpResponse
from apstatus.models import ips
from django.template import loader
import datetime


def index(request):
    data = ips.objects.all()
    now = datetime.datetime.now()
    hour=int(now.hour)
    hour1=hour-1
    hour2=hour-2
    hour3=hour-3
    hour4=hour-4
    hour5=hour-5
    hour6=hour-6
    hour7=hour-7
    hour8=hour-8
    hour9=hour-9
    hour10=hour-10
    hour11=hour-11
    template = loader.get_template('apstatus/index.html')
    context = {
        'data':data,
        'hour':hour,
        'hour1':hour1,
        'hour2':hour2,
        'hour3':hour3,
        'hour4':hour4,
        'hour5':hour5,
        'hour6':hour6,
        'hour7':hour7,
        'hour8':hour8,
        'hour9':hour9,
        'hour10':hour10,
        'hour11':hour11,
    }
    return HttpResponse(template.render(context, request))

