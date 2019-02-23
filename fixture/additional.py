

class MH:
    def __init__(self, app):
        self.app = app

    def change_element(self, element, element_name):
        wd = self.app.wd
        wd.find_element_by_name(element).click()
        wd.find_element_by_name(element).clear()
        wd.find_element_by_name(element).send_keys(element_name)

    def edit_group(self, name, header, footer):
        MH.change_element(self, "group_name", name)
        MH.change_element(self, "group_header", header)
        MH.change_element(self, "group_footer", footer)

    def edit_user(self, name, last, nick, title, tel, mail):
        MH.change_element(self, "firstname", name)
        MH.change_element(self, "lastname", last)
        MH.change_element(self, "nickname", nick)
        MH.change_element(self, "title", title)
        MH.change_element(self, "home", tel)
        MH.change_element(self, "email", mail)
