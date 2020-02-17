from career import Career
from locators import CareerPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class CareerPage(BasePage):

    def faculty_panels(self):
        """Retrieves all faculty panels from the catalog page"""
        return self.driver.find_elements(*CareerPageLocators.PANEL)

    def extract_code(self,string):
        """Extracts the career code from the innerHTML of li"""
        if string == '':
            return ''
        else:
            code_wt=string.split('<span>')[1]
            code = code_wt.rstrip('</span>')
            return code

    def extract_name(self,string):
        """Extracts the career name from the innerHTML of li"""

        if string == '':
            return ''
        else:
            name = string.split(" <")[0]
            return name

    def extract_faculty_english(self,string):
        """Extracts the name of the faculty in english language"""
        if string == '':
            return ''
        else:
            faculty = string.split(")")[1]
            return faculty

    def careers(self):
        """Retrieves the careers and returns a list of careers back"""
        #Retrieve the panels where the info is
        panels = self.faculty_panels()
        #Initialize the list of careers
        careers = []
        #For loop to extract the panel data
        for panel in panels:
            #Heading has the faculty name
            faculty = self.extract_faculty_english(panel.find_element(*CareerPageLocators.PANEL_HEADING).text)
            #Career list is within a ul, each item is li
            career_list = panel.find_elements(*CareerPageLocators.ITEM)
            for career in career_list:
                #getting the innerHTML of the li item
                li_html=career.get_attribute("innerHTML")
                #appending the object Career
                careers.append(Career(self.extract_name(li_html),
                                      self.extract_code(li_html),
                                      faculty,
                                      career.find_element(*CareerPageLocators.LINK).get_attribute("href")))
        return careers