from selenium import webdriver
from fixture.session import SH
from fixture.group import GH
from fixture.user import UH
from fixture.additional import MH


class Applicaton:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SH(self)
        self.group = GH(self)
        self.user = UH(self)
        self.additional = MH(self)


    def destroy(self):
        self.wd.quit()
