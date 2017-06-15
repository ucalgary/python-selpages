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
                 css=None, xpath=None):
        args = locals()
        self._locators = [(_LOCATORS[arg], args[arg]) for arg, by in _LOCATORS.items() if args.get(arg)]
        self._multiple = multiple

    @property
    def locators(self):
        return self._locators
