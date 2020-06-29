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
import test
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

        driver = webdriver.Chrome(executable_path=os.environ.get(
            "CHROMEDRIVER_PATH"), options=chrome_options)

        driver.get("https://globalsearch.cuny.edu/CFGlobalSearchTool/search.jsp")

        # initial page
        college = driver.find_element_by_id("QNS01")
        college.click()
        term = driver.find_element_by_xpath(
            "//*[contains(text(), 'Fall Term')]")
        term.click()
        nextBtn = driver.find_element_by_class_name("SSSBUTTON_CONFIRMLINK")
        nextBtn.click()

        # second page
        subject = driver.find_element_by_xpath(
            "//*[contains(text(), 'Computer Science')]")
        subject.click()
        courseCareer = driver.find_element_by_xpath(
            "//*[contains(text(), 'Undergraduate')]")
        courseCareer.click()
        showOpenClass = driver.find_element_by_id("open_classId")
        if(showOpenClass.is_selected()):
            showOpenClass.click()
        searchBtn = driver.find_element_by_id("btnGetAjax")
        searchBtn.click()

        # list of classes page
        # sections = ["48158", "48201", "51617", "48196", "48220"]
        sections = ["48170", "48194", "48186", "48149",
                    "48224", "48216", "48225", "48218"]
        for section in sections:
            driver.find_element_by_id("imageDivLink_inst0").click()
            # find a way to choose dropdown by name and not id

            # driver.find_element_by_id("imageDivLink21").click()
            driver.find_element_by_id("imageDivLink8").click()

            element = driver.find_element_by_xpath(
                "//*[contains(text(), '" + section + "')]")
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            element.click()

            driver.find_element_by_xpath(
                "//*[contains(text(), '" + section + "')]").click()

            print("checking status...")
            status = driver.find_element_by_id(
                "SSR_CLS_DTL_WRK_SSR_DESCRSHORT")
            classStatus = status.text
            print("class is", classStatus)

            if(classStatus == "Open"):
                myclass = test.sms()
                myclass.sendSmsTo("3474663815", section)
            # time.sleep(50)
            driver.back()

        time.sleep(5)
        print("closing window...")
        driver.quit()
        time.sleep(5)
    except Exception as e:
        print(e)
