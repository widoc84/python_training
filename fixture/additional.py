import random
import string


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

    def edit_user(self,name,last,nick,title,address,homephone,mobilephone,workphone,secondaryphone,email1,email2,email3):
        MH.change_element(self, "firstname", name)
        MH.change_element(self, "lastname", last)
        MH.change_element(self, "nickname", nick)
        MH.change_element(self, "title", title)
        MH.change_element(self, "address", address)
        MH.change_element(self, "home", homephone)
        MH.change_element(self, "mobile", mobilephone)
        MH.change_element(self, "work", workphone)
        MH.change_element(self, "phone2", secondaryphone)
        MH.change_element(self, "email", email1)
        MH.change_element(self, "email2", email2)
        MH.change_element(self, "email3", email3)

    def random_string(prefix, maxlen):
        symbols = string.ascii_letters + string.digits
        return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def random_number(maxlen):
        symbols = string.digits
        return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def random_email(maxlen):
        symbols = string.ascii_letters
        return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@ya.ru"
