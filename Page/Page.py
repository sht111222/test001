from Page.login_page import Login_Page
from Page.setting_page import Setting_Page
from Page.add_address_page import Add_Address_Page

class Page:
    def __init__(self, driver):
        self.driver = driver
    def get_login_page(self):
        # 返回登陆实例化对象
        return Login_Page(self.driver)
    def get_setting_page(self):
        # 返回设置实例化对象
        return Setting_Page(self.driver)
    def get_add_addr_page(self):
        # 返回添加地址实例化对象
        return Add_Address_Page(self.driver)

