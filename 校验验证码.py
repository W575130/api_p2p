import requests

# 校验用户名是否存在
url = 'http://localhost/index.php?ctl=ajax&act=check_field&fhash=VEvtAQVvVYHVazjguRDtcHXGTtrJbLHsLpnBTushljhWUoUlyW '
data = {
    'field_name': 'user_name',
    'field_data': 'wwj'
}
result = requests.post(url=url,data=data)
print(result.json())