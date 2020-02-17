from selenium.webdriver.common.by import By

class CareerPageLocators(object):
    """A class for career page locators. All career page locators are here"""
    PANEL = (By.CLASS_NAME,'panel')
    PANEL_HEADING = (By.CLASS_NAME,'panel-title')
    PANEL_BODY = (By.CLASS_NAME,'panel-body')
    ITEM = (By.CSS_SELECTOR,'ul:last-of-type li')
    LINK = (By.TAG_NAME,"a")
