import requests
import unittest


# 使用类的方式来管理http请求的发送，它是爷爷类

class BaseHttp(object):
    host = 'http://localhost'

    # 统一http发送方式
    def sendHttp(self, path, method='post', **kwargs):
        # url通过拼接方式传参
        url = '{}{}'.format(self.host, path)
        result = requests.request(method=method, url=url, **kwargs)
        return result


class VerifyClass(unittest.TestCase):
    # 校验状态码
    # 校验json格式响应体
    # text/html格式响应体
    # 校验响应体的特殊字段
    def verify_json_data(self, target, key, result_data):
        code = target.status_code
        target = target.json()
        self.assertEqual(200, code)
        self.assertEqual(target.get(key), result_data)

    def verify_html_data(self, target, result_data):
        code = target.status_code
        target = target.text
        self.assertEqual(200, code)
        self.assertEqual(result_data, target)
