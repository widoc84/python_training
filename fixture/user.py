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
        add.edit_user(self, user.username, user.last_name, user.nickname, user.title, user.address, user.homephone, user.mobilephone,
                      user.workphone, user.secondaryphone, user.email, user.email2, user.email3)
        wd.find_element_by_xpath("//input[21]").click()#confirm
        self.open_home_page()
        self.user_cache = None

    def change_by_index(self,index, user):
        wd = self.app.wd
        self.open_home_page()
        user = user
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        add.edit_user(self, user.username, user.last_name, user.nickname, user.title, user.address, user.homephone, user.mobilephone,
                      user.workphone, user.secondaryphone, user.email,user.email2,user.email3)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.user_cache = None

    def change_by_id(self,id, user):
        wd = self.app.wd
        self.open_home_page()
        el =wd.find_element_by_css_selector("input[value='%s']" % id)
        el.find_element_by_xpath("//img[@alt='Edit']").click()
        user = user
        add.edit_user(self, user.username, user.last_name, user.nickname, user.title, user.address, user.homephone, user.mobilephone,
                      user.workphone, user.secondaryphone, user.email,user.email2,user.email3)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.user_cache = None

    def delete_by_index(self, indexid):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_id(str(indexid)).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.user_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_id(str(id)).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
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
#            for element in wd.find_elements_by_css_selector("tr"):
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                last = cells[1].text
                user = cells[2].text
                address = cells[3].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_email = cells[4].text
                self.user_cache.append(User(last_name=last, username=user, id=id, address=address, all_phone=all_phones,all_email=all_email))
        return (self.user_cache)

    def open_contact_to_edit_by_id(self,id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("tr[name='entry'] a[href*='edit.php?id=%s']" % id).click()

    def open_contact_view_by_id(self,id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("tr[name='entry'] a[href*='vcard.php?id=%s']" % id).click()


    def get_user_info_from_edit(self, id):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        username = wd.find_element_by_name("firstname").get_attribute("value")
        last = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return User(last_name=last,
                    username=username,
                    address=address,
                    homephone=homephone,
                    workphone=workphone,
                    mobilephone=mobilephone,
                    secondaryphone=secondaryphone,
                    email=email,
                    email2=email2,
                    email3=email3,
                    id=id)
