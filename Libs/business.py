from Libs.tools import BaseHttp


class LoginClass(BaseHttp):
    cookies = {
        'PHPSESSID': ''
    }

    # 封装公共业务模块
    def loginApi(self):
        login_path = '/index.php?ctl=user&act=dologin'
        login_data = {
            'email': 'wwjaaaa8',
            'user_pwd': 'cktkRW5XSHJnQlpwUWVDZVNiR2NPTUNocEZXcnNJbEhrY1J0YURBSlFhc2FTWFRKeUMlMjV1NjVCOSUyNXU3RUY0QWExMjM0NTYlMjV1OEY2RiUyNXU0RUY2',
            'auto_login': '1',
            'ajax': '1',
        }
        login_result = self.sendHttp(path=login_path, data=login_data)
        phpid = login_result.cookies['PHPSESSID']
        self.cookies['PHPSESSID'] = phpid
        return login_result
