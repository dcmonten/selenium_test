from selenium import webdriver
import chromedriver_binary
import page
import csv


class ESPOLSearchCareer():
    def search_careers(self):
        """Retrieves the careers from the ESPOL page"""
        #Load the main page.
        main_page = page.CareerPage(self.driver)
        #Get the careers
        careers=main_page.careers()
        #Putting the carrers in a csv file
        with open('careers.csv', 'w', newline='\n') as outcsv:
            writer = csv.writer(outcsv)
            writer.writerow(["career_name_en",
                             "career_code",
                             "faculty_name",
                             "link_to_career_curriculum"])
            for career in careers:
                writer.writerow([career.name,
                                 career.code,
                                 career.faculty,
                                 career.link])

    def tearDown(self):
        self.driver.close()


    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.espol.edu.ec/es/educacion/grado/catalogo")
        self.search_careers()
        self.tearDown()


if __name__ == "__main__":
    #Executing the career retriever
    ESPOLSearchCareer()