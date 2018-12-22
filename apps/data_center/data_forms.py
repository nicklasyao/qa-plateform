from django import forms
from django.forms import widgets

operation_field = forms.CharField(label='操作人id', initial='4552764896e647e894fed159c3e80898',
                                  widget=widgets.TextInput(attrs={'size': '30'}),
                                  help_text='默认yytest', disabled=True)


# 房源
class AddHouseForm(forms.Form):
    raiseNo = forms.CharField(label='认筹号', initial='raise1001')
    roomId = forms.CharField(label='房间代码', initial='room1001')
    projectId = forms.CharField(label='项目代码', initial='yxwbgy')
    applyAmount = forms.IntegerField(label='申请分期金额', initial='990000')
    editUserId = operation_field
    # order_id = forms.CharField(label='订单编号', initial='', disabled=True)
    productCode = forms.CharField(label='产品编号(新增进件时必须传)', initial='0000041')
    productId = forms.CharField(label='产品Id(新增进件时必须传)', initial='977018b4cf46459890a030d8d43bcb8b', widget=widgets.TextInput(attrs={'size': '30'}))


# 销售顾问信息
class AddPointSaleForm(forms.Form):
    editUserId = operation_field
    orderId = forms.CharField(label='订单编号', initial='PLD0000000163')
    pointsale = forms.CharField(label='销售顾问', initial='蔡工')
    pointsalePhone = forms.CharField(label='销售顾问电话', initial='18820010110')
    # productCode = forms.CharField(label='产品编号(新增进件时必须传)', initial='0000005')
    # productId = forms.CharField(label='产品Id(新增进件时必须传)', initial='3e4fac7e20df4e95884d349a1901aeb2',widget=widgets.TextInput(attrs={'size': '30'}))


class AddPayInfoForm(forms.Form):
    editUserId = operation_field
    accountName = forms.CharField(label='银行卡户名', initial='蔡蔡')
    certId = forms.CharField(label='身份证号码', initial='441283199506184165')
    accountNo = forms.CharField(label='还款银行卡号', initial='6216617008000485728')
    accountMobile = forms.CharField(label='银行卡预留手机号', initial='15578955071')
    repaymentBankNo = forms.CharField(label='开户行', initial='C10104', disabled=True)
    branchBankProvince = forms.CharField(label='开户行所在省份', initial='110000', disabled=True)
    branchBankCity = forms.CharField(label='开户行所在城市', initial='110200', disabled=True)
    repaymentSubBankNo = forms.CharField(label='开户行分行', initial='北京', disabled=True)
    bankBranch = forms.CharField(label='开户行支行', initial='望京', disabled=True)
    # productCode = forms.CharField(label='产品编号(新增进件时必须传)', initial='0000005')
    # productId = forms.CharField(label='产品Id(新增进件时必须传)', initial='3e4fac7e20df4e95884d349a1901aeb2',widget=widgets.TextInput(attrs={'size': '30'}))
    serialNo = forms.CharField(label='订单编号', initial='PLD0000000163')


class AddCustomerForm(forms.Form):
    editUserId = operation_field
    customerName = forms.CharField(label='姓名', initial='诸葛亮')
    certId = forms.CharField(label='身份证号码', initial='441283199506184165')
    serialNo = forms.CharField(label='订单编号', initial='PLD0000000163')


class ApprovalForm(forms.Form):
    editUserId = operation_field
    serialNo = forms.CharField(label='订单编号', initial='PLD0000000163')
