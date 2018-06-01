from selenium.webdriver.common.by import By
"""
    个人中心页面
"""
# 我的按钮
my_btn = (By.XPATH, "//*[contains(@text,'我的') and contains(@resource-id,'com.tpshop.malls:id/tab_txtv')]")
# 登陆/注册按钮-id
insert_login = (By.XPATH, "//*[contains(@text,'登录/注册')]")
# 收货地址按钮
recive_address = (By.XPATH, "//*[contains(@text,'收货地址')]")

"""
    登陆页面
"""
# 登陆用户名
login_name = (By.ID, "com.tpshop.malls:id/edit_phone_num")
# 登陆密码
login_passwd = (By.ID, "com.tpshop.malls:id/edit_password")
# 登陆按钮
login_btn = (By.ID, "com.tpshop.malls:id/btn_login")
# 登陆成功页面,判断我的订单是否存在
login_suc_mes = (By.XPATH, "//*[contains(@text,'我的订单') and contains(@resource-id,'com.tpshop.malls:id/title_txtv')]")
# 登陆页面点击关闭按钮
login_page_close = (By.ID, "com.tpshop.malls:id/titlebar_back_rl")
"""
    个人中心
"""
"""
    个人中心 - 设置页面
"""
# 设置按钮
person_setting_btn = (By.ID, "com.tpshop.malls:id/setting_btn")
# 退出按钮
logout_btn = (By.ID, "com.tpshop.malls:id/exit_btn")

"""
    收货地址页面
"""
# 新增收货地址
add_rec_address_btn = (By.ID, "com.tpshop.malls:id/add_address_btn")
# 收货人
add_rec_name = (By.ID, "com.tpshop.malls:id/consignee_name_edtv")
# 手机号
add_rec_phone = (By.ID, "com.tpshop.malls:id/consignee_mobile_edtv")
# 所在地区
add_rec_area = (By.ID, "com.tpshop.malls:id/consignee_region_txtv")
# 所在地区 - 省 北京
add_rec_area_bj = (By.XPATH, "//*[contains(@text,'北京')]")
# 所在地区 - 省 - 市
add_rec_area_bj_sxq = (By.XPATH, "//*[contains(@text,'市辖区')]")
# 所在地区 - 省 - 市 - 区/县
add_rec_area_bj_sxq_dcq = (By.XPATH, "//*[contains(@text,'东城区')]")
# 所在地区 - 省 - 市 - 区/县 - 镇/街道
add_rec_area_bj_sxq_dcq_dhm = (By.XPATH, "//*[contains(@text,'东华门')]")
# 所在地区确定按钮
add_rec_area_acc_btn = (By.ID, "com.tpshop.malls:id/btn_right")
# 详细地址
add_rec_detail_addr = (By.ID, "com.tpshop.malls:id/consignee_address_edtv")
# 默认设置按钮
add_rec_default_btn = (By.ID, "com.tpshop.malls:id/set_default_sth")
# 删除按钮
add_rec_delete_btn = (By.XPATH, "//*[contains(@text,'删除') and contains(@class,'android.widget.TextView')]")
# 删除弹窗确认按钮
add_rec_delete_alert_acc = (By.ID, "com.tpshop.malls:id/positiveButton")
# 保存收货地址按钮
add_rec_save_btn = (By.ID, "com.tpshop.malls:id/submit_btn")
# 判断添加收货人 例如：hello
add_rec_name_list = (By.ID, "com.tpshop.malls:id/address_consignee_txtv")
# 判断是否为默认地址
add_rec_list_default = (By.ID, "com.tpshop.malls:id/address_default_txtv")
# 修改收货人地址按钮
add_rec_list_edit = (By.ID, "com.tpshop.malls:id/address_edit_btn")
