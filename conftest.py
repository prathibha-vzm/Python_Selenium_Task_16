#Imported pytest and webdriver
import os
import pytest
from pytest_html import extras
from selenium import webdriver

# This is the Start-up Fixture setting up the environment
@pytest.fixture()
def set_up():
    option=webdriver.ChromeOptions()
    option.add_argument("--disable-notifications")
    driver=webdriver.Chrome(option)
    driver.get("https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live")
    driver.maximize_window()
    return driver

# This tear_down will automatically run to close the webpage
@pytest.fixture(autouse=True)
def tear_down(set_up):
    driver=set_up
    yield
    driver.close()

#It will execute after the test run
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def report_generator_with_screenshot(item,call):
#     outcome=yield
#     report=outcome.get_result() #outcome will fetch all the test results
#
#     if report.when=="call" and report.failed:
#         driver=item.funcargs.get("set_up")
#         if driver:
#             try:
#                 report_dir = "screenshots"
#
#                 os.makedirs(report_dir, exist_ok=True)
#                 file_name = os.path.join(report_dir, f"{item.name}.png")
#                 driver.save_screenshot(file_name)
#                 print(f"Screenshots are saved to {report_dir}")
#                 screenshot = driver.get_screenshot_as_base64()
#
#                 report.extras.append(extras.image(screenshot, name=f"screenshot {item.name}"))
#
#             except Exception as e:
#                   report.extras.append(extras.text(f"Failed to capture screenshot: {str(e)}"))














