import logging


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
