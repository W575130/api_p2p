import requests
import sql_test

# 手机号码
mobile = 13500112224
user_name = 'wwjaaaa9'
idno = '452121199908221590'
real_name = 'wwjaaaa9'
# 发送短信验证码

# 短信url
verify_url = 'http://localhost/index.php?ctl=ajax&act=get_register_verify_code&fhash=VEvtAQVvVYHVazjguRDtcHXGTtrJbLHsLpnBTushljhWUoUlyW'
sms_data = {
    'user_mobile': '{}'.format(mobile),
    'smsverify': 'aaaa',
}
# 发送短信验证请求
result = requests.post(url=verify_url, data=sms_data)
# 通过数据库获取短信验证码
sms = sql_test.readMSN(mobile=mobile)

## 获取校验用户名的sessionID
session_url = 'http://localhost/index.php?ctl=ajax&act=check_field'
session_data = {
    'field_name': 'user_name',
    'field_data': '{}'.format(user_name),
}
r = requests.post(url=session_url, data=session_data)
# 将headers返回值赋予data
data_cookies = r.headers
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
    'Cookie': '{}'.format(phpid2)
}

# 注册第一步接口的业务流
register_url = 'http://localhost/index.php?ctl=user&act=doregister'
register_data = {
    'user_type': 0,
    'user_name': '{}'.format(user_name),
    'mobile': '{}'.format(mobile),
    'smsverify': 'aaaa',
    'sms_code': sms,
    'user_pwd': 'Aa123456',
    'user_pwd_confirm': 'Aa123456',
    'referer': '',
    'agreement': 1,
    'commit': '注册',
}

# 发送业务流的第一步注册
result2 = requests.post(url=register_url, data=register_data, headers=headers2)
print('注册成功', result2.text)

# 实名制验证
name_url = 'http://localhost/index.php?ctl=user&act=do_re_name_id'
name_data = {
    'real_name': '{}'.format(user_name),
    'idno': '{}'.format(idno),
    'sex': '-1',
    'byear': '1999',
    'bmonth': '08',
    'bday': '26',
    'commit': '验证',
}
result3 = requests.post(url=name_url, data=name_data, headers=headers2)
print('实名制成功', result3.text)
