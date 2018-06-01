from Base.Base import Base
import Page, allure
class Add_Address_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    @allure.step(title="点击个人收货地址按钮")
    def click_recv_addr(self):
        # 点击个人中心收货地址
        self.click_element(Page.recive_address)

    @allure.step(title="点击收货地址列表中新建地址按钮")
    def new_address(self):
        # 点击新建地址
        self.click_element(Page.add_rec_address_btn)

    @allure.step(title="新建地址页面添加收货人")
    def add_recv_name(self, name="hello"):
        # 输入收货人
        self.input_element(Page.add_rec_name, name)
        allure.attach("描述","收货人为:%s" % name)

    @allure.step(title="新建地址页面添加手机号")
    def add_recv_phone(self, phone="13488834010"):
        # 输入手机号
        self.input_element(Page.add_rec_phone, phone)
        allure.attach("描述", "收货人手机号:%s" % phone)

    @allure.step(title="新建地址页面选择所在区域，默认设置为北京-市辖区-东城区-东华门街道")
    def add_recv_change_area(self):
        # 选择所在区域
        # 点击所在地区
        self.click_element(Page.add_rec_area)
        # 点击北京市
        self.click_element(Page.add_rec_area_bj)
        # 点击市辖区
        self.click_element(Page.add_rec_area_bj_sxq)
        # 点击东城区
        self.click_element(Page.add_rec_area_bj_sxq_dcq)
        # 点击东华门街道
        self.click_element(Page.add_rec_area_bj_sxq_dcq_dhm)
        # 点击所在地区确定按钮
        self.click_element(Page.add_rec_area_acc_btn)

    @allure.step(title="新建地址页面添加详细地址")
    def add_recv_detail(self, detail_addr="北七家"):
        # 输入详细地址
        self.input_element(Page.add_rec_detail_addr, detail_addr)
        allure.attach("描述", "详细地址为:%s" % detail_addr)

    @allure.step(title="新建地址页面点击设置默认地址按钮")
    def click_default_btn(self):
        # 点击默认地址开关
        self.click_element(Page.add_rec_default_btn)

    @allure.step(title="新建地址页面点击点击保存")
    def click_addr_save(self):
        # 点击新增地址保存按钮
        self.click_element(Page.add_rec_save_btn)

    @allure.step(title="返回当前地址收货人列表")
    def if_addr_name(self):
        # 判断收货人姓名是否正确
        try:
            name_list = self.search_elements(Page.add_rec_name_list, timeout=5)
            text_list = [i.text for i in name_list]
            allure.attach("描述","当前地址收货人列表为:%s" % str(text_list))
            return text_list
        except:
            return False

    @allure.step(title="判断默认是否存在当前地址列表中")
    def if_addr_default(self):
        # 判断是否有默认
        try:
            default_list = self.search_elements(Page.add_rec_list_default, timeout=5)
            text_def_list = [i.text for i in default_list]
            allure.attach("描述","默认表示列表为:%s" % str(text_def_list))
            return text_def_list
        except:
            return False

    @allure.step(title="点击编辑地址按钮")
    def edit_address(self):
        # 修改收货人地址
        self.click_element(Page.add_rec_list_edit)

    @allure.step(title="点击编辑页面删除按钮")
    def delete_address(self):
        # 删除地址
        self.click_element(Page.add_rec_delete_btn)
        # 删除确认按钮
        self.click_element(Page.add_rec_delete_alert_acc)