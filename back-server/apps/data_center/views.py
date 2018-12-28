from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests, json
from . import service_urls, data_forms

req_headers = {'content-type': 'application/json'}
               # 'X-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pblVzZXJJZCI6IjI4YTBhMTJlMTYxZDQyYmY5MzFlZDM3NmNkZTg0YWQxIiwiaXNzIjoiU2VydmljZSIsImV4cCI6MTU0NTkwMDE0NSwiaWF0IjoxNTQ1MDM2MTQ1fQ.WijjtSDnUsAXtfcHE1jxxi9RWGpdU1b6bf8OjUCDWy0'}


# Create your views here.
def data_home(req):
    return render(req, "fyfq/data_index.html")


def json_resp(req):
    return JsonResponse({'msg': 'ok', 'data': 'test'})


# def test(req):
# return post_request(req, service_urls.add_customer, data_forms.AddCustomerForm, 'test.html')

def get_province(req):
    provinces = requests.get(service_urls.list_province)
    return render(req, "fyfq/data_index.html", {'msg': provinces.json()})


def add_house(req):
    return post_request(req, service_urls.add_house)


def add_point_sale(req):
    return post_request(req, service_urls.add_pointsale)


def add_pay_info(req):
    return post_request(req, service_urls.add_payment_info)


def add_customer(req):
    return post_request(req, service_urls.add_customer)


def auto_approve(req):
    return post_request(req, service_urls.auto_approve, data_forms.ApprovalForm, 'fyfq/auto_approve.html')


# 公共方法
def post_request(req, url):
    if req.method == 'POST':
        print(json.loads(req.body))
        # print(url)
        rsp = requests.post(url, req.body, headers=req_headers)
        print('rsp-->', rsp.json())
        return JsonResponse(_get_response_json_dic(rsp.json()))
    else:
        return JsonResponse(_get_response_json_dic('', -1, '无效请求'))


# 封装rest结果
def _get_response_json_dic(data, code=0, message='Success'):
    result_data = {
        'code': code,
        'message': message,
        'data': data
    }
    return result_data
