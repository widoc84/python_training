import time
from fixture.additional import MH as add
from model.group import Group


class GH:
    def __init__(self, app):
        self.app = app

    def delete(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_name("delete").click()
        self.open_group_page()
        self.group_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_name("delete").click()
        self.open_group_page()
        self.group_cache = None

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
#edit form
        add.edit_group(self,group.name, group.header, group.footer)
        wd.find_element_by_name("submit").click()
        self.open_group_page()
#wait for check
        time.sleep(2)
        self.group_cache = None

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def edit_by_index(self, index, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_name("edit").click()
        add.edit_group(self, group.name, group.header, group.footer)
        wd.find_element_by_name("update").click()
        self.open_group_page()
        self.group_cache = None

    def edit_by_id(self, id, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_name("edit").click()
        add.edit_group(self, group.name, group.header, group.footer)
        wd.find_element_by_name("update").click()
        self.open_group_page()
        self.group_cache = None

    def edit(self, group):
        self.edit_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache=[]
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text,id=id))
        return (self.group_cache)

