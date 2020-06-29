# 1 redirect to globalsearch
# 2 choose college and term
# 3 choose subject, course career, and uncheck show open classes
# 4 find the dropdown to open by text ex: 'CSCI 381'
# 5 find the classes of interest by ClassNo.
# 6 iterate through specified classes check if any are open
# 7 repeat 4 - 6
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from functions import *
import os

classStatus = "Closed"

while(True):
    try:
        print("reopening window...")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_PATH")

        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

        # base url
        driver.get("https://globalsearch.cuny.edu/CFGlobalSearchTool/search.jsp")

        # initial page
        college = driver.find_element_by_id("QNS01")
        college.click()
        term = driver.find_element_by_xpath("//*[contains(text(), 'Fall Term')]")
        term.click()
        nextBtn = driver.find_element_by_class_name("SSSBUTTON_CONFIRMLINK")
        nextBtn.click()

        # second page
        subject = driver.find_element_by_xpath("//*[contains(text(), 'Computer Science')]")
        subject.click()
        courseCareer = driver.find_element_by_xpath("//*[contains(text(), 'Undergraduate')]")
        courseCareer.click()
        showOpenClass = driver.find_element_by_id("open_classId")
        if(showOpenClass.is_selected()):
            showOpenClass.click()
        searchBtn = driver.find_element_by_id("btnGetAjax")
        searchBtn.click()

        # sections to check
        sections335 = ["48202"]
        open_sections_and_check(driver, sections335, "14")

        sections344 = ["48164"]
        open_sections_and_check(driver, sections344, "17")

        sections363 = ["48160"]
        open_sections_and_check(driver, sections363, "19")

        sections381 = ["48158", "48201", "51617", "48196", "48220"]
        open_sections_and_check(driver, sections381, "21")

        time.sleep(5)
        print("closing window...")
        driver.quit()
        time.sleep(5)
    except Exception as e:
        print(e)
