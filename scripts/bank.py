import unittest
from Libs.business import LoginClass
from Libs.tools import VerifyClass
from po.MyP2P.BankCard import BankCardApi


class TestBankCard(VerifyClass):

    # def setUp(self):
    #     # 实例化绑定银行卡类
    #     bc = BankCardApi()

    def test_bind_success001(self):
        # 实例化绑定银行卡类
        bc = BankCardApi()
        # 发送银行卡请求
        result = bc.bindBankCard()
        # 校验数据正确性
        self.verify_json_data(result,'info','保存成功')

    def test_bind_success002(self):
        # 实例化绑定银行卡类
        bc = BankCardApi()
        # 发送银行卡请求
        result = bc.bindBankCard()
        # 校验数据正确性
        self.verify_json_data(result, 'info', '该银行卡已存在')


if __name__ == '__main__':
    unittest.main(verbosity=2)
