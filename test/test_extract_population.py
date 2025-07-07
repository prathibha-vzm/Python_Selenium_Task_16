#Importing pytest to use the mark, Exceptions are imported
import pytest
from selenium.common import TimeoutException, ElementNotVisibleException
# Class is imported
from test_population.Pages.extract_population_page import WorldCounts
import keyboard #Keyboard is imported to check the keyboard activity

# Marked this as Sanity test
@pytest.mark.sanity
#To test the test_population class and its methods
def test_world_counts(set_up):
    driver=set_up
    world_count=WorldCounts(driver) # Creating object for class
    counter = get_world_count.population_counts() #Calling the methods
    world_count.click_dismiss_cookies()
    print("\nWorld Population")
    while True:
        try:
            print(counter.text)                # To print the test_population counts on console
            if keyboard.is_pressed('Ctrl+C'):  # Condition to check Ctrl+C is pressed
                print("Closed the page by pressing on Ctrl+C")
                break
        except (TimeoutException,ElementNotVisibleException):  #Exceptions are handled
            print("Press Ctrl+C to Stop")

if __name__=='__main__': # To run the code on Terminal
    test_world_counts()  #Calling the test logic method







