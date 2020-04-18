from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from pynput.mouse import Listener # Para detección de clicks
import logging
import os 
import time 
import pyautogui #For using mouse


#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s: %(message)s')

#Opening a new tab and avoiding the pop up notifications from chrome
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
#Getting into the URL
driver.get("https://auth.laureate.net/adfs/ls/?SAMLRequest=hVNNb%2BIwEL33V6DcSRwgVWuRSCzsBxILCNge9rIy9mRrKbGznklL%2F32dhBZ2VWV9sTKe997Mm8kURVlUfFbTo9nBnxqQbgb%2BnMrCIG8f06B2hluBGrkRJSAnyfez7ys%2BChmvnCUrbRH8A%2BtHCURwpK3pYMtFGmzWn1ebr8v1L8ViMUrY8TgSt%2Bx%2Bcj8%2BMoiPLInZeHwrJxJylYzvIO%2BgD%2BDQ86SBp%2B0iW2eftAK39qppsNBYFeJl0HydxRBrWBokYcjD2IgN2WQYxwd2x5OEJ5OfXd7Ce6GNoJb9kahCHkXCGxUWonYgCEIDFAmVY1Rg9C7e2vFJG6XN734Xjl0S8m%2BHw3a43ewPHcnszZ25NViX4PbgnrSEH7vVpZJSl7VRNqwrE4KqwwqixvdRJCQGWcszbQK87ddl%2F8WVQEKRmEbXqAtPxRsLl4utLbR8aePN%2BWJdKai%2Fzyai1TBvU3nVTAwJDAXvLLOisM%2Fz1tQ0IFdDMIj%2B0j7vJqh2U70vBCcazG1ZCaexmRCchKRz45fmr9PnhV%2B7HeRZ72ZKLps8H97669k61cwUpNc%2BOGGwso7OHn1I3lUd9ZSd3bw9X%2F922Ss%3D&RelayState=https%3A%2F%2Fmimundo.upn.edu.pe%2Fsaml-success")


def log_in():
    email = input("Email: ")
    password = input("Password: ")
    try:
        while True:    
            time.sleep(3)
            user = driver.find_element_by_id('userNameInput')
            user.send_keys(email)
            time.sleep(3)
            password = driver.find_element_by_id('passwordInput')
            password.send_keys(password)
            time.sleep(3)
            button = driver.find_element_by_id('submitButton')
            button.click()  
            break
    except NoSuchElementException:
        print('Not found')
    
def getting_into():
    while True:
        time.sleep(3)
        try: 
            close = driver.find_element_by_class_name('fa.fa-close')
            close.click()
        except:
            pass
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,1000)")    
        time.sleep(3)
        driver.get('''https://upn.blackboard.com/auth-saml/saml/login?apId=_111_1&  redirectUrl=https%3A%2F%2Fupn.blackboard.com%2Fwebapps%2Fportal%2Fexecute%2FdefaultTab''')
        time.sleep(3)
        accept = driver.find_element_by_class_name('button-1')
        accept.click()
        time.sleep(3)
        driver.get("https://upn.blackboard.com/webapps/blackboard/execute/modulepage/view?course_id=_1355492_1&cmp_tab_id=_409291_1&mode=view")
        time.sleep(3)
        driver.get("""https://upn.blackboard.com/webapps/blackboard/content/launchLink.jsp?course_id=_1355492_1&tool_id=_1852_1&tool_type=TOOL&mode=view&mode=reset""")
        time.sleep(5)
        pyautogui.moveTo(397,440,duration=0)
        pyautogui.click(397,440)
        pyautogui.moveTo(1073,431,duration=0)
        #join 
        count = 1
        while True: #Do 5 clicks per second
            pyautogui.click(1073,431)            
            time.sleep(1)
            count+=1
            if count == 5:
                break 
                
        time.sleep(18)
        pyautogui.moveTo(389,221,duration=0)
        pyautogui.click(389,221)
        time.sleep(5)
        try:
            pyautogui.moveTo(1281,211,duration=0)
            pyautogui.click(1281,211)
            time.sleep(5)
        except:
            pass
        pyautogui.moveTo(902,204,duration=0)    
        pyautogui.click(902,204)
        time.sleep(5)
        pyautogui.moveTo(1281,211,duration=0)
        pyautogui.click(1281,211)
    
        #Creating a lambda function which is going to return the position once we do clicks
        click = lambda x,y,button,pressed: print(f'pressed: {pyautogui.position()}')
        while True:
            with Listener(on_click=click) as listener:
                listener.join()    
                time.sleep(60)
            break    

log_in()
getting_into()