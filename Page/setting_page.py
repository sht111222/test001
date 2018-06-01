from Base.Base import Base
import Page, allure


class Setting_Page(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)
    @allure.step(title="个人信息页面点击设置按钮")
    def click_setting_btn(self):
        # 点击个人中心设置按钮
        self.click_element(Page.person_setting_btn)

    @allure.step(title="设置页面点击退出按钮")
    def click_logout_btn(self):
        # 点击退出登陆按钮
        self.click_element(Page.logout_btn)