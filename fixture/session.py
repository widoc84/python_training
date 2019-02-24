import time

class SH:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)

        wd.find_element_by_id("LoginForm").submit()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if len(wd.find_elements_by_link_text("Logout")) > 0:
            self.logout()
        else:
            pass

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0


    def is_logged_in_as(self, username):
        wd = self.app.wd
#        return  wd.find_element_by_xpath("xpath = (.// *[normalize-space(text()) and normalize - space(.)='Address Book'])[1] / preceding::b[1]").text == "(" + username + ")"
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "(" + username + ")"


