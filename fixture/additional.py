

class MH:
    def __init__(self, app):
        self.app = app

    def change_element(self, element, element_name):
        wd = self.app.wd
        wd.find_element_by_name(element).click()
        wd.find_element_by_name(element).clear()
        wd.find_element_by_name(element).send_keys(element_name)
