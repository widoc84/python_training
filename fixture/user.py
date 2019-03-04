import time
from fixture.additional import MH as add
from model.user import User


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
        time.sleep(2)#check
        self.user_cache = None

    def change_by_index(self,index, user):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        add.edit_user(self, user.username, user.last_name, user.nickname, user.title, user.tel, user.mail)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        time.sleep(2)#check
        self.user_cache = None


    def delete_by_index(self, indexid):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_id(str(indexid)).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        time.sleep(2)#check
        self.user_cache = None


    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.user_cache=[]
            for element in wd.find_elements_by_css_selector("tr"):
                if element.text != 'Last name First name Address All e-mail All phones':
                    last = element.find_elements_by_tag_name("td")[1].text
                    user = element.find_elements_by_tag_name("td")[2].text
                    id = element.find_element_by_name("selected[]").get_attribute("value")
                    self.user_cache.append(User(last_name=last, username=user, id=id))
                else:
                    pass
        return (self.user_cache)
