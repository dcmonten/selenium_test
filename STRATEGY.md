# Strategy
## Reading the HTML

1. Search for the container using inspect element.
2. Each faculty name is at the div with class panel heading.
3. Undergraduate programs is inside a p strong within the div with panel class.
4. Each li item has the career name with the career code enclosed in a span tag, the career link is in the a tag.
 

## Reading about selenium and page model object

Since I'm new to selenium and page object model, I read the docs you've sent by email and the available resources.


## Create the basic scripts

### locators.py
 Panel locator gets the panel with a single faculty information, this selector helps us getting all elements with class `panel`.
    `PANEL = (By.CLASS_NAME,'panel')`
   
 Panel heading locator helps sus find the faculty name, which is a tag with class `panel-title`
    `PANEL_HEADING = (By.CLASS_NAME,'panel-title')`
 
 Item gives us all the li tags within the last ul, this contains the information of each career in english.
   `ITEM = (By.CSS_SELECTOR,'ul:last-of-type li')`
 Link gives us the a tag, this will be useful for retrieving the links.
 
    `LINK = (By.TAG_NAME,"a")`
    
 ### page.py
 
 After creating the base object as the documentation suggests for Page Object Model, we created the class `CareerPage(BasePage)` 
 within this class we have a method to get the faculty panels, which returns the panels with the faculty information, using the PANEL locator. 

The extraction methods are applied to strings with html tags to retrieve information.

Extract code gets the career code from the span tag within the li innerHTML.

Extract name gets the career name from the li innerHTML. 
   
Extract faculty english gets the faculty name in english by spliting the full name from the panel title. 

Careers returns a list of careers, it works by analizing each panel, getting the faculty name and the list of li items containing the career information of the second ul tag, for every tag we retrieve the name, code and link, and then create an object which is stored in the careers list.  
   
## main.py 

Finally, the class `ESPOLSearchCareer()` is the one calling http://www.espol.edu.ec/es/educacion/grado/catalogo to get the list of careers using the `CareerPage` class and saving them in a csv file with name "careers.csv".
 

