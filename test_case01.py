import scripts01

def test():
    # login_result = scripts01.login_api()
    headers2 = scripts01.login_api()
    prepay_result = scripts01.prepay_api(headers2)
    # # 校验statuscode
    # if prepay_result.status_code == 200:
    #     print('测试成功')

    # 校验接口的某个字段
    if '立即支付' in prepay_result.text:
        return '线下充值支付成功'
    else:
        return '支付失败'

if __name__ == '__main__':
    data = test()
    print(data)