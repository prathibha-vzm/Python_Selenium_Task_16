#Importing Exception, Wait, Expected_Conditions and By
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Creating a class to fetch the counting data and close the cookies if any
class WorldCounts:
    #Using Constructor to include XPATH and driver
    def __init__(self,driver):
        self.driver=driver
        self.counter_ticker=(By.XPATH,
                             "//div[@class='counter-ticker is-size-2-mobile']")
        self.wait=WebDriverWait(driver,10) # Explicit wait
        self.cookies=(By.XPATH,
                      "//a[@aria-label='dismiss cookie message']")
        #Fluent wait used
        self.fluent_wait=WebDriverWait(driver,timeout=10,poll_frequency=5,ignored_exceptions=[NoSuchElementException])

    #This method is used to locate the test_population counting element and handling Exception that might occur
    #Used wait to find the element
    def get_population_counts(self):
        try:
             counter=self.wait.until(expected_conditions.visibility_of_element_located(self.counter_ticker))
             return counter
        except TimeoutException:
            print("TimeOut Exception")

    #This method is used to locate the cookies in the page and click on it, Handled the exception
    def click_dismiss_cookies(self):
        try:
            dismissing = self.fluent_wait.until(expected_conditions.visibility_of_element_located(self.cookies))
            if dismissing.is_displayed(): #If the element is located, it will be clicked
              dismissing.click()
        except TimeoutException: # Either it will throw Exception
            print("No cookies found")

