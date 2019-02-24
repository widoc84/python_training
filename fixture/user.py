import time
from fixture.additional import MH as add


class UH:
    def __init__(self, app):
        self.app = app

    def add(self, user):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()#openuser
        #edit form
        add.edit_user(self, user.username, user.last_name, user.nickname, user.title, user.tel, user.mail)
        wd.find_element_by_xpath("//input[21]").click()#confirm
        self.open_home_page()
        time.sleep(5)#check

    def change(self, user):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        add.edit_user(self, user.username, user.last_name, user.nickname, user.title, user.tel, user.mail)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        time.sleep(5)#check

    def delete(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        time.sleep(5)#check

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()
