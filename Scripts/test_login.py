import sys, os
sys.path.append(os.getcwd())

import pytest
from Base.Read_Data import Read_Data
from Page.Page import Page
from Base.get_driver import get_driver


def get_login_data():
    list_data = []
    data = Read_Data("login_data.yml").get_test_data()
    for i in data.values():
        list_data.append((i.get("username"),i.get("passwd"),i.get("expect"),
                          i.get("expect_toast"),i.get("get_msg")))
    return list_data


class Test_Login:
    def setup_class(self):
        self.page_obj = Page(get_driver())
        # 点击我的
        self.page_obj.get_login_page().click_my_btn()
    def teardown_class(self):
        self.page_obj.driver.quit()


    @pytest.mark.parametrize("username,passwd,expectx,expect_toast,get_msg",get_login_data())
    def test_login(self, username,passwd,expectx,expect_toast,get_msg):
        # 点击登陆/注册
        self.page_obj.get_login_page().click_insert_login()
        # 登陆操作
        self.page_obj.get_login_page().login(username, passwd)

        if expectx:
            try:
                # 登陆成功toast消息
                suc_msg = self.page_obj.get_login_page().find_toast(get_msg)
                # 获取我的订单按钮是否存在 成功返回True 不成功返回False
                suc_status = self.page_obj.get_login_page().get_suc_login_status()
                # 断言成功/失败
                assert suc_msg == expect_toast and  suc_status, self.page_obj.get_login_page().screen_shot()
                # 退出操作
                # 点击个人中心设置
                self.page_obj.get_setting_page().click_setting_btn()
                # 点击退出登录按钮
                self.page_obj.get_setting_page().click_logout_btn()
            except:
                self.page_obj.get_login_page().screen_shot()
                # 点击登陆页面关闭按钮
                self.page_obj.get_login_page().login_faile_x()
                assert False
        else:
            # 获取toast消息
            reslut_msg = self.page_obj.get_login_page().find_toast(get_msg)
            # 点击登陆页面关闭按钮
            self.page_obj.get_login_page().login_faile_x()
            assert expect_toast == reslut_msg, self.page_obj.get_login_page().screen_shot()



