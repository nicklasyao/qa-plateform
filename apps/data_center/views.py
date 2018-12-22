from django.shortcuts import render
from django.http import HttpResponse
import requests, json
from . import service_urls, data_forms

req_headers = {'content-type': 'application/json',
               'X-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pblVzZXJJZCI6IjI4YTBhMTJlMTYxZDQyYmY5MzFlZDM3NmNkZTg0YWQxIiwiaXNzIjoiU2VydmljZSIsImV4cCI6MTU0NTkwMDE0NSwiaWF0IjoxNTQ1MDM2MTQ1fQ.WijjtSDnUsAXtfcHE1jxxi9RWGpdU1b6bf8OjUCDWy0'}


# Create your views here.
def data_home(req):
    return render(req, "data_index.html")


# def test(req):
    # return post_request(req, service_urls.add_customer, data_forms.AddCustomerForm, 'test.html')

def get_province(req):
    provinces = requests.get(service_urls.list_province)
    return render(req, "data_index.html", {'msg': provinces.json()})


def add_house(req):
    return post_request(req, service_urls.add_house, data_forms.AddHouseForm, 'add_house.html')


def add_point_sale(req):
    return post_request(req, service_urls.add_pointsale, data_forms.AddPointSaleForm, 'add_point_sale.html')


def add_pay_info(req):
    return post_request(req, service_urls.add_payment_info, data_forms.AddPayInfoForm, 'add_pay_info.html')


def add_customer(req):
    return post_request(req, service_urls.add_customer, data_forms.AddCustomerForm, 'add_customer.html')


def auto_approve(req):
    return post_request(req, service_urls.auto_approve, data_forms.ApprovalForm, 'auto_approve.html')


# 公共方法
def post_request(req, url, form_name, template_name):
    if req.POST:
        req_form = form_name(req.POST)
        if req_form.is_valid():
            rsp = requests.post(url, json.dumps(req_form.cleaned_data), headers=req_headers)
            print(rsp)
            return render(req, template_name, {'form': req_form, 'result_data': rsp.json()})
        else:
            print('数据校验失败: ', rsp.errors)
            return render(req, template_name, {'form': req_form, 'result_data': req_form.errors})
    else:
        f = form_name()
        return render(req, template_name, {'form': f})
