from Base.Base import Base
import Page, allure

class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self,driver)
    @allure.step(title="点击首页我的按钮")
    def click_my_btn(self):
        # 点击我的按钮
        self.click_element(Page.my_btn)

    @allure.step(title="点击个人中心页面登陆/注册")
    def click_insert_login(self):
        # 点击登陆/注册
        self.click_element(Page.insert_login)

    @allure.step(title="等页面信息操作")
    def login(self, phone="13488834010", passwd="159357"):
        # 登陆操作
        allure.attach("登陆用户信息","登陆用户名:%s\n登陆的密码:%s" % (phone, passwd))
        # 输入用户名
        self.input_element(Page.login_name, phone)
        # 输入密码
        self.input_element(Page.login_passwd, passwd)
        # 点击登陆按钮
        self.click_element(Page.login_btn)

    @allure.step(title="登陆成功页面我的订单判断")
    def get_suc_login_status(self):
        # 判断是否登陆成功，成功返回True 不成功返回False
        try:
            self.search_element(Page.login_suc_mes, timeout=10)
            allure.attach("我的订单","存在，认定登陆成功")
            return True
        except Exception as e:
            return False

    @allure.step(title="关闭登陆页面")
    def login_faile_x(self):
        # 点击登陆页面关闭按钮
        self.click_element(Page.login_page_close)

    @allure.step(title="判断用户是否为登陆状态")
    def if_login(self):
        # 判断是否为登陆状态
        # 点击我的
        self.click_my_btn()
        try:
            # 判断是否有登陆/注册
            self.search_element(Page.insert_login, timeout=5)
            allure.attach("登陆","用户为未登陆状态")
            # 点击登陆注册
            self.click_insert_login()
            # 执行登陆操作
            self.login()
            allure.attach("登陆", "登陆成功")
        except:
            allure.attach("登陆", "用户已为登陆状态")
            pass
