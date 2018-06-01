import sys, os, pytest
sys.path.append(os.getcwd())

from Base.get_driver import get_driver
from Page.Page import Page

class Test_001:

    def setup_class(self):
        self.page_obj = Page(get_driver())
        self.page_obj.get_login_page().if_login()
    def teardown_class(self):
        self.page_obj.driver.quit()
    @pytest.mark.run(order=1)
    def test_add_addr(self):
        # 点击收货地址，新增收货地址
        self.page_obj.get_user_addr_page().click_addr_btn()
        # 添加用户名
        self.page_obj.get_user_addr_page().addr_name()
        # 添加手机号
        self.page_obj.get_user_addr_page().addr_phone()
        # 选择所在地区
        self.page_obj.get_user_addr_page().addr_area()
        # 添加详细地址
        self.page_obj.get_user_addr_page().addr_detail()
        # 勾选默认地址
        self.page_obj.get_user_addr_page().addr_default()
        # 保存收货地址
        self.page_obj.get_user_addr_page().addr_save_btn()

        assert self.page_obj.get_user_addr_page().get_recive_address()
        assert self.page_obj.get_user_addr_page().get_addr_default()

    @pytest.mark.run(order=3)
    def test_delete_addr(self):
        self.page_obj.get_user_addr_page().update_addr_btn()

        self.page_obj.get_user_addr_page().delete_addr()
        assert "删除成功" == self.page_obj.get_user_addr_page().find_toast("删除")

        assert not self.page_obj.get_user_addr_page().get_recive_address()

    @pytest.mark.run(order=2)
    def test_update_addr(self):
        # 修改收货地址
        self.page_obj.get_user_addr_page().update_addr_btn()

        self.page_obj.get_user_addr_page().addr_name(name="1234")
        self.page_obj.get_user_addr_page().addr_default()
        self.page_obj.get_user_addr_page().addr_save_btn()

        assert self.page_obj.get_user_addr_page().get_recive_address()
        assert "编辑成功" == self.page_obj.get_user_addr_page().find_toast("编辑")

        assert not self.page_obj.get_user_addr_page().get_addr_default()

