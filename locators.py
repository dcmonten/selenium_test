from selenium.webdriver.common.by import By

class CareerPageLocators(object):
    """A class for career page locators. All career page locators are here"""
    GO_BUTTON = (By.ID, 'submit')
    PANEL = (By.CLASS_NAME,'panel')
    PANEL_HEADING = (By.CLASS_NAME,'panel-title')
    PANEL_BODY = (By.CLASS_NAME,'panel-body')

