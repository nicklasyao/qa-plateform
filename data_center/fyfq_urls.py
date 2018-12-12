# coding=utf-8
"""
凤凰分期服务, REST url
"""
# url前缀
fyfq_prefix = 'http://47.107.21.127:9000/api/fyfq'

# 身份查询
list_province = fyfq_prefix + '/backend/houses/area/getProvince'
# 新增房源
add_house = fyfq_prefix + '/backend/houses/staging/apply/updateHouseApplyInfoById'