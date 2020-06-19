# import time;
# import os;

# while True:
#     print("Hello from python")
#     os.system("heroku ps:restart web.1")
#     time.sleep(80)


# 1 redirect to globalsearch
# 2 choose college and term
# 3 choose subject, course career, and uncheck show open classes
# 4 find the dropdown to open by text ex: 'CSCI 381'
# 5 find the row of interest by ClassNo. text
# 6 stay in the same <tr> and look at the status image
# 7 refresh the page
# 8 repeat 4 - 7
from selenium import webdriver
import time
import test
import os

classStatus = "Closed"
# while(True):

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_PATH")

driver = webdriver.Chrome(
    executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

driver.get("https://globalsearch.cuny.edu/CFGlobalSearchTool/search.jsp")

# initial page
college = driver.find_element_by_id("QNS01")
college.click()
term = driver.find_element_by_xpath("//*[contains(text(), 'Fall Term')]")
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
sections = ["48158", "48201", "51617", "48196", "48220"]
for section in sections:
    driver.find_element_by_id("imageDivLink_inst0").click()
    # find a way to choose dropdown by name and not id
    driver.find_element_by_id("imageDivLink21").click()

    driver.find_element_by_xpath(
        "//*[contains(text(), '" + section + "')]").click()

    print("checking status...")
    status = driver.find_element_by_id("SSR_CLS_DTL_WRK_SSR_DESCRSHORT")
    classStatus = status.text
    print("class is", classStatus)

    if(classStatus == "Open"):
        myclass = test.sms()
        myclass.sendSmsTo("3474663815", section)
    # time.sleep(50)
    driver.back()

    # time.sleep(5)
    # stream = os.popen(
    #     "kill $(ps aux | grep chrome | grep -v grep | awk '{print $2}')")
    # output = stream.read()
    # print(output)

    # stream = os.popen(
    #     "kill $(ps aux | grep google | grep -v grep | awk '{print $2}')")
    # output = stream.read()
    # print(output)


# CSCI 335-31
# (48202)

# CSCI 344-10
# (48164)

# CSCI 363-33
# (48160)

# CSCI 381-12
# (48158)

# CSCI 381-13
# (48201)

# CSCI 381-15
# (51617)

# CSCI 381-22
# (48196)

# CSCI 381-51
# (48220)

# MATH 231-03
# (43700)

# MATH 231-08
# (43705)
