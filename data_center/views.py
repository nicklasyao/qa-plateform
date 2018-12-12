from django.shortcuts import render
from django.http import HttpResponse
import requests
from . import fyfq_urls, data_forms


# Create your views here.
def data_home(req):
    return render(req, "data_index.html")


def get_province(req):
    provinces = requests.get(fyfq_urls.list_province)
    return render(req, "data_index.html", {'msg': provinces.json()})


def add_house(req):
    if req.POST:
        ahf = data_forms.AddHouseForm(req.POST)
        if ahf.is_valid():
            print(ahf.cleaned_data)
            return render(req, 'add_house.html', {'form': ahf, 'result_data':'XXXXXXXXXXXXxx'})
        else:
            return render(req, 'add_house.html', {'form': ahf, 'msg': ahf.errors})
    else:
        f = data_forms.AddHouseForm()
        return render(req, 'add_house.html', {'form': f})



