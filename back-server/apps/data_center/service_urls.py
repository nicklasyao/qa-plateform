# coding=utf-8
from django.conf import settings
"""
凤凰分期服务, REST url
"""
# url前缀
fyfq_prefix = settings.FYFQ_URL + '/api/fyfq/'
risk_prefix = settings.FYFQ_URL + '/api/risk/'

# 身份查询
list_province = fyfq_prefix + '/backend/houses/area/getProvince'
# 新增房源
add_house = fyfq_prefix + '/backend/houses/staging/apply/updateHouseApplyInfoById'
# 新增销售顾问信息
add_pointsale = fyfq_prefix + '/backend/houses/staging/apply/updatePointSaleById'
# 还款账户信息
add_payment_info = fyfq_prefix + '/backend/houses/staging/apply/updateOrderBankInfoByOrderId'
# 客户
add_customer = fyfq_prefix + '/backend/houses/cusinfo/getCusIdInsertCerIdAndName'

"""
risk
"""
# 自动审批
auto_approve = risk_prefix + '/backend/pedate/automati/capproval'