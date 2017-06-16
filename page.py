import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


log = logging.getLogger(__name__)


class Page(object):
    """Represents a web page

    The `Page` class represents web pages and their elements. It should be subclassed for different types of web pages
    with class level `Element` instances assigned to provides access to elements on instances of the class.

    The following is an example of a login pass class with that provides access to username and password inputs and
    a login button.

        class LoginPage(Page):
            username = Element(id='loginForm:userName')
            password = Element(id='loginForm:password')
            login = Element(id='loginForm:loginButton')

    The `LoginPage` class can then be used to fill in the username and password inputs and log in to an app.

        driver = webdriver.PhantomJS()
        driver.get('https://sandbox.rms-dev.ucalgary.ca/converis/secure/login')
        page = LoginPage(driver)
        page.username = 'configadmin'
        page.password = 'converis'
        page.login.click()
    """
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
    """Provides access to elements on a page

    The `Element` class works in conjuntion with `Page` objects to provide access to elements on a web page. Values for
    any of the eight Selenium element locator types can be used to specify how elements are to be found. If multiple
    locator types are used, then locators will be used in the following order until elements are found.

        id, name, tag, class_name, link, partial_link, selector, xpath

    None is returned if no elements are found for all specified locators.

    This class is intended to be accessed as properties on `Page` instances. The `__get__` and `__set__` descriptor
    methods are implemented to get Selenium elements and set values on those elements.
    """
    def __init__(self, id=None, name=None, tag=None, class_name=None, link_text=None, partial_link_text=None,
                 css=None, xpath=None, multiple=False):
        args = locals()
        self._locators = [(_LOCATORS[arg], args[arg]) for arg, by in _LOCATORS.items() if args.get(arg)]
        self._multiple = multiple
        log.debug(f'Initialized {self.__class__.__name__} with locators: {self.locators}')

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
        log.debug(f'No elements found for locators: {self.locators}')
        return None

    def __get__(self, instance, owner):
        if not instance:
            return None

        context = instance.webdriver

        return self.find(context)

    def __set__(self, instance, value):
        elements = self.__get__(instance, instance.__class__)
        if not elements:
            raise ValueError('Cannot set value because no elements could be found')

        if self.multiple:
            [e.send_keys(value) for e in elements]
        else:
            elements.send_keys(value)
