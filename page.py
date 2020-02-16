from element import BasePageElement
from locators import CareerPageLocators


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class CareerPage(BasePage):
    """Home page action methods come here."""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def faculty_names(self):
        """Verifies that the hardcoded text "ESPOL" appears in page title"""
        return self.driver.find_elements(*CareerPageLocators.PANEL_HEADING)



class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source