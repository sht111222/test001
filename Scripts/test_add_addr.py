import sys, os, pytest
sys.path.append(os.getcwd())
from Base.Read_Data import Read_Data
from Base.get_driver import get_driver
from Page.Page import Page

def data_list():
    # 添加收货地址列表
    add_list_data = []
    # 编辑地址列表
    edit_list_data = []
    # 删除数据列表
    del_list_data = []
    data = Read_Data("add_address_data.yml").get_test_data()

    for i in data.get("Add_Data").values():
        add_list_data.append((i.get("name"),i.get("phone"),i.get("detail"),
                          i.get("get_toast"),i.get("expect_toast"),i.get("expect_default")))

    for o in data.get("Edit_Data").values():
        edit_list_data.append((o.get("name"), o.get("get_toast"), o.get("expect_toast")))

    for x in data.get("Del_data").values():
        del_list_data.append((x.get("name"), x.get("get_toast"), x.get("expect_toast")))

    return {"add_data": add_list_data, "edit_data": edit_list_data, "del_data": del_list_data}

class Test_Add_Address():

    def setup_class(self):
        self.pag_obj = Page(get_driver())
        # 判断是否登陆
        self.pag_obj.get_login_page().if_login()
    def teardown_class(self):
        self.pag_obj.driver.quit()

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("name, get_toast, expect_toast", data_list().get("del_data"))
    def test_delete_addr(self, name, get_toast, expect_toast):
        # 删除已添加地址
        # 地址编辑按钮
        self.pag_obj.get_add_addr_page().edit_address()
        # 点击删除
        self.pag_obj.get_add_addr_page().delete_address()
        # 判断toast消息
        assert expect_toast == self.pag_obj.get_add_addr_page().find_toast(get_toast)
        # 判断列表收货人不包含某个用户名
        assert not self.pag_obj.get_add_addr_page().if_addr_name()


    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name, get_toast, expect_toast",data_list().get("edit_data"))
    def test_edit_address(self, name, get_toast, expect_toast):
        # 修改收货人 和 取消默认
        self.pag_obj.get_add_addr_page().edit_address()
        # 修改收货人
        self.pag_obj.get_add_addr_page().add_recv_name(name)
        # 关闭默认开关
        self.pag_obj.get_add_addr_page().click_default_btn()
        # 点击保存按钮
        self.pag_obj.get_add_addr_page().click_addr_save()
        # 判断toast消息
        assert expect_toast == self.pag_obj.get_add_addr_page().find_toast(get_toast)
        # 判断收货人
        assert name in self.pag_obj.get_add_addr_page().if_addr_name()
        # 判断默认消失
        assert not self.pag_obj.get_add_addr_page().if_addr_default()

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name,phone,detail,get_toast,expect_toast,expect_default",data_list().get("add_data"))
    def test_add_address(self,name,phone,detail,get_toast,expect_toast,expect_default):
        # 点击收货地址
        self.pag_obj.get_add_addr_page().click_recv_addr()
        # 点击新建地址
        self.pag_obj.get_add_addr_page().new_address()
        # 输入收货人
        self.pag_obj.get_add_addr_page().add_recv_name(name)
        # 输入手机号
        self.pag_obj.get_add_addr_page().add_recv_phone(phone)
        # 选择所在地区
        self.pag_obj.get_add_addr_page().add_recv_change_area()
        # 输入详细地址
        self.pag_obj.get_add_addr_page().add_recv_detail(detail)
        # 点击保存新增地址
        self.pag_obj.get_add_addr_page().click_addr_save()

        # 判断添加成功提示
        assert expect_toast == self.pag_obj.get_add_addr_page().find_toast(get_toast)
        # 判断收货人姓名
        assert name in self.pag_obj.get_add_addr_page().if_addr_name()
        # 判断默认
        assert  expect_default in self.pag_obj.get_add_addr_page().if_addr_default()