from Libs.business import LoginClass

class BankCardApi(LoginClass):
    # 绑定银行卡业务
    def bindBankCard(self):
        # 调用登录
        self.loginApi()
        # 绑定数据接口的path
        bind_path = '/member.php?ctl=uc_money&act=savebank'
        # 绑定数据接口的数据
        bind_data = {
            'real_name': 'wwjaaaa8',
            'bank_id': '1',
            'otherbank': '',
            'region_lv1': '1',
            'region_lv2': '6',
            'region_lv3': '77',
            'region_lv4': '705',
            'bankzone': 'aaaa',
            'bankcard': '6228 3333 4455 555',
            'reBankcard': '6228 3333 4455 555'
        }
        # 发送请求
        result = self.sendHttp(path=bind_path,data=bind_data,cookies=self.cookies)
        return result


