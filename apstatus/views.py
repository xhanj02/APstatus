from django.shortcuts import render
from django.http import HttpResponse
from apstatus.models import ips
from django.template import loader
import datetime


def index(request):
    data = ips.objects.all()
    hour=(datetime.datetime.now()- datetime.timedelta(minutes=60)).hour
    hour1=(datetime.datetime.now()- datetime.timedelta(hours= 1)).hour
    hour2=(datetime.datetime.now()- datetime.timedelta(hours= 2)).hour
    hour3=(datetime.datetime.now()- datetime.timedelta(hours= 3)).hour
    hour4=(datetime.datetime.now()- datetime.timedelta(hours= 4)).hour
    hour5=(datetime.datetime.now()- datetime.timedelta(hours= 5)).hour
    hour6=(datetime.datetime.now()- datetime.timedelta(hours= 6)).hour
    hour7=(datetime.datetime.now()- datetime.timedelta(hours= 7)).hour
    hour8=(datetime.datetime.now()- datetime.timedelta(hours= 8)).hour
    hour9=(datetime.datetime.now()- datetime.timedelta(hours= 9)).hour
    hour10=(datetime.datetime.now()- datetime.timedelta(hours= 10)).hour
    hour11=(datetime.datetime.now()- datetime.timedelta(hours= 11)).hour
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

