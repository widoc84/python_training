import time
from fixture.additional import MH as add



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
        add.change_element(self, "group_name", group.name)
        add.change_element(self, "group_header", group.header)
        add.change_element(self, "group_footer", group.footer)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()
#wait for check
        time.sleep(5)

    def edit(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        add.change_element(self, "group_name", group.name)
        add.change_element(self, "group_header", group.header)
        add.change_element(self, "group_footer", group.footer)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("groups").click()
        time.sleep(5)
