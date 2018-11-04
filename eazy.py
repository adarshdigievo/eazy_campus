from	selenium	import	webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import sys
import time

browser	=	webdriver.Firefox()
browser.get('http://210.212.227.210/tkmce/index.aspx')
userElem	=	browser.find_element_by_id('txtUserName')

userElem.send_keys(sys.argv[1])   #admn no here

passwordElem	=	browser.find_element_by_id('txtPassword')

passwordElem.send_keys(sys.argv[2]) # password here
# A new captcha field was introduced in the eazy campus website, which require the user to enter the captcha.
# Providing a time gap for the user to enter the captcha
time.sleep(15)
loginElem	=	browser.find_element_by_id('btnLogin')
loginElem.click()
try:
    WebDriverWait(browser, 20).until(EC.alert_is_present(),
                                   'Timed out waiting for staff eval popup to appear.')
    alert = browser.switch_to_alert()
    alert.accept()
    print "alert accepted"
except TimeoutException:
    print "no alert"
    
#Change in Content Placeholder name
sEval	=	browser.find_element_by_id('ctl00_ContentPlaceHolder1_dlAlertLIst_dlAlertDisplay_ctl00_HyperLink2')
sEval.click()
try:
    WebDriverWait(browser, 20).until(EC.alert_is_present(),
                                   'Timed out waiting for second popup to appear.')
    alert = browser.switch_to_alert()
    alert.accept()
    print "alert accepted"
except TimeoutException:
    print "no alert"
while (1):
    try:
        elems = browser.find_elements_by_xpath("//a[@href]")
        elem=elems[0]
        i=0
        str1=elem.get_attribute("href")
        while str1.find('staffname')==-1:
            i=i+1
            elem=elems[i]
            str1=elem.get_attribute("href")
        print str1
        elem.click()
        try:
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_gvQuestionsList_ctl02_rbtn_Choice_1_0")))
        finally:
            # TODO - make a loop to iterate and click below radio buttons
             radio1= 	browser.find_element_by_id('ctl00_ContentPlaceHolder1_gvQuestionsList_ctl02_rbtn_Choice_1_0')
             radio1.click()
             radio1= 	browser.find_element_by_id('ctl00_ContentPlaceHolder1_gvQuestionsList_ctl03_rbtn_Choice_2_0')
             radio1.click()
             radio1= 	browser.find_element_by_id('ctl00_ContentPlaceHolder1_gvQuestionsList_ctl04_rbtn_Choice_3_0')
             radio1.click()
             radio1= 	browser.find_element_by_id('ctl00_ContentPlaceHolder1_gvQuestionsList_ctl05_rbtn_Choice_4_0')
             radio1.click()
             radio1= 	browser.find_element_by_id('ctl00_ContentPlaceHolder1_gvQuestionsList_ctl06_rbtn_Choice_5_0')
             radio1.click()
             radio1= 	browser.find_element_by_id('ctl00_ContentPlaceHolder1_gvQuestionsList_ctl07_rbtn_Choice_6_0')
             radio1.click()
             radio1= 	browser.find_element_by_id('ctl00_ContentPlaceHolder1_gvQuestionsList_ctl08_rbtn_Choice_7_0')
             radio1.click()
             radio1= 	browser.find_element_by_id('ctl00_ContentPlaceHolder1_gvQuestionsList_ctl09_rbtn_Choice_8_0')
             radio1.click()
             radio1= 	browser.find_element_by_id('ctl00_ContentPlaceHolder1_gvQuestionsList_ctl10_rbtn_Choice_9_0')
             radio1.click()
             radio1= 	browser.find_element_by_id('ctl00_ContentPlaceHolder1_gvQuestionsList_ctl11_rbtn_Choice_10_0')
             radio1.click()
             radio1= 	browser.find_element_by_id('ctl00_ContentPlaceHolder1_gvQuestionsList_ctl12_rbtn_Choice_11_0')
             radio1.click()
             btnsave=   browser.find_element_by_id('ctl00_ContentPlaceHolder1_btnSave')
             btnsave.click()
             try:
                WebDriverWait(browser, 10).until(EC.alert_is_present(),
                                                'Timed out waiting for second popup to appear.')
                alert = browser.switch_to_alert()
                alert.accept()
                print "alert accepted"
             except TimeoutException:
                 print "no alert"


    except:
        print "Staff evaluation completed :)"
        break
