import time


def change_element(self, element, element_name):
    wd = self.app.wd
    wd.find_element_by_name(element).click()
    wd.find_element_by_name(element).clear()
    wd.find_element_by_name(element).send_keys(element_name)

class UH:
    def __init__(self, app):
        self.app = app

    def add(self, user):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()#openuser
        #edit form
        change_element(self, "firstname", user.username)
        change_element(self, "lastname", user.last_name)
        change_element(self, "nickname", user.nickname)
        change_element(self, "title", user.title)
        wd.find_element_by_name("theform").click()
        change_element(self, "home", user.tel)
        change_element(self, "email", user.mail)
        wd.find_element_by_xpath("//input[21]").click()#confirm
        wd.find_element_by_link_text("home").click()
        time.sleep(5)#check

    def change(self, user):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
#        wd.find_element_by_id("19").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        change_element(self, "firstname", user.username)
        change_element(self, "lastname", user.last_name)
        change_element(self, "nickname", user.nickname)
        change_element(self, "title", user.title)
#        wd.find_element_by_name("theform").click()
        change_element(self, "home", user.tel)
        change_element(self, "email", user.mail)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home").click()
        time.sleep(5)#check

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        time.sleep(5)#check
