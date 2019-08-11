import requests

# 线性模型
login_url = 'http://localhost/index.php?ctl=user&act=dologin'
login_data = {
    'email': 'wwjaaaa6',
    'user_pwd': 'cktkRW5XSHJnQlpwUWVDZVNiR2NPTUNocEZXcnNJbEhrY1J0YURBSlFhc2FTWFRKeUMlMjV1NjVCOSUyNXU3RUY0QWExMjM0NTYlMjV1OEY2RiUyNXU0RUY2',
    'auto_login':'1',
    'ajax': '1',
}
login_result = requests.post(url=login_url,data=login_data)
# 将headers返回值赋予data
data_cookies = login_result.headers
# 打印出data的值
print(data_cookies)
# 获取Set_Cookie字段的内容
Set_Cookie = data_cookies['Set-Cookie']
# 将Set_Cookie字段的内容存在一个列表中，以分号为分割符，进行分割
phpid_list = Set_Cookie.split(';')
# phpid1赋值：取列表中的第一个值
phpid1 = phpid_list[0]
# phpid2赋值：列表中的第二个分割值再以“， ”进行分割，取第二个值
phpid2 = phpid_list[3].split(', ')[2]
# 打印出phpid1与phpid2的值
print('phpid1=', phpid1)
print('phpid2=', phpid2)
# 优化后添加的数据是
headers2 = {
    'Cookie': '{}'.format(phpid1)
}

# 线下充值业务
prepay_url = 'http://localhost/member.php?ctl=uc_money&act=incharge_done'
pre_pay_data = {
    'check_ol_bl_pay': 'on',
    'money': '999',
    'pingzheng': '',
    'memo': '1234567',
    'payment': '5',
    'bank_id': '0',
}
prepay_result = requests.post(prepay_url,data=pre_pay_data,headers=headers2)
# 校验statuscode
if prepay_result.status_code == 200:
    print('测试成功')

# 校验接口的某个字段
if '立即支付' in prepay_result.text:
    print('测试成功')