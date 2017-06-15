from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Page(object):

    def __init__(self, webdriver):
        if webdriver is None:
            raise ValueError('webdriver must not be None')
        self._webdriver = webdriver

    @property
    def webdriver(self):
        return self._webdriver


_LOCATORS = {
    'id': By.ID,
    'name': By.NAME,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,
    'link': By.LINK_TEXT,
    'partial_link': By.PARTIAL_LINK_TEXT,
    'selector': By.CSS_SELECTOR,
    'xpath': By.XPATH
}


class Element(object):

    def __init__(self, id=None, name=None, tag=None, class_name=None, link_text=None, partial_link_text=None,
                 css=None, xpath=None, multiple=False):
        args = locals()
        self._locators = [(_LOCATORS[arg], args[arg]) for arg, by in _LOCATORS.items() if args.get(arg)]
        self._multiple = multiple

    @property
    def locators(self):
        return self._locators

    @property
    def multiple(self):
        return self._multiple

    def find(self, context):
        f = context.find_elements if self.multiple else context.find_element
        for locator in self.locators:
            try:
                return f(*locator)
            except NoSuchElementException:
                pass
        return None
