from selenium import webdriver
from fixture.session import SH
from fixture.group import GH
from fixture.user import UH
from fixture.additional import MH


class Applicaton:
    def __init__(self, browser="chrome", base_url="http://localhost/addressbook/"):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognazed browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SH(self)
        self.group = GH(self)
        self.user = UH(self)
        self.additional = MH(self)
        Applicaton.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
