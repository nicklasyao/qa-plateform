from django import forms
from django.forms import widgets


class AddHouseForm(forms.Form):
    raise_no = forms.CharField(label='认筹号', initial='raise1001')
    room_id = forms.CharField(label='房间代码', initial='room1001')
    project_id = forms.CharField(label='项目代码', initial='CSCS')
    apply_amount = forms.IntegerField(label='申请分期金额', initial='500000')
    edit_user = forms.CharField(max_length=1000, label='操作人id',initial='fa78828d0a4a48f5bf92676bf45d86af', widget=widgets.TextInput(attrs={'size': '30'}))
    # order_id = forms.CharField(label='订单编号', initial='', disabled=True)
    product_code = forms.CharField(label='产品编号(新增进件时必须传)', initial='0000005')
    product_id = forms.CharField(label='产品Id(新增进件时必须传)', initial='83e418ddbc23405892f13499842f3970', widget=widgets.TextInput(attrs={'size': '30'}))


