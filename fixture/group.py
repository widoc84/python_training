import time


def change_element(self, element, element_name):
    wd = self.app.wd
    wd.find_element_by_name(element).click()
    wd.find_element_by_name(element).clear()
    wd.find_element_by_name(element).send_keys(element_name)

class GH:
    def __init__(self, app):
        self.app = app

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("groups").click()
        time.sleep(5)

    def create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
#edit form
        change_element(self, "group_name", group.name)
        change_element(self, "group_header", group.header)
        change_element(self, "group_footer", group.footer)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()
#wait for check
        time.sleep(5)

    def edit(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        change_element(self, "group_name", group.name)
        change_element(self, "group_header", group.header)
        change_element(self, "group_footer", group.footer)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("groups").click()
        time.sleep(5)
