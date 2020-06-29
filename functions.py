from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from sms import *


def open_sections_and_check(driver, sections, linkNum):
    for section in sections:
        # finds this section and clicks it's link
        open_section(driver, section, linkNum)

        # check this sections' status
        check_section_status(driver, section)

        driver.back()
    return


def open_section(driver, section, linkNum):
    # initial dropdown
    driver.find_element_by_id("imageDivLink_inst0").click()

    # find a way to choose dropdown by name and not id
    # course's dropdown
    driver.find_element_by_id("imageDivLink"+linkNum).click()

    # find section number
    element = driver.find_element_by_xpath(
        "//*[contains(text(), '" + section + "')]")

    # move to element then click
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.click()
    return


def check_section_status(driver, section):
    print("checking status...")

    # gets the sections' status
    status = driver.find_element_by_id("SSR_CLS_DTL_WRK_SSR_DESCRSHORT")
    classStatus = status.text

    print("class is", classStatus)

    # if section is open notify user
    if(classStatus == "Open"):
        myclass = Sms()
        myclass.sendSmsTo("3474663815", section)

    return
