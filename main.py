from selenium import webdriver
import chromedriver_binary
import page

class ESPOLSearchCareer():
    """A sample test class to show how page object works"""
    def search_careers(self):
        """
        """
        #Load the main page. In this case the home page of Python.org.
        main_page = page.CareerPage(self.driver)
        fcnames=main_page.faculty_names()
        for name in fcnames:
            if name.text == '':
                continue
            else:
                eng_name=name.text.split(")\n")
                print (eng_name[1])

    def tearDown(self):
        self.driver.close()


    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.espol.edu.ec/es/educacion/grado/catalogo")
        self.search_careers()
        self.tearDown()


if __name__ == "__main__":
    ESPOLSearchCareer()