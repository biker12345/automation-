'''  program to automate the automate the login and browser surfing '''

#-----------import area----------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import subprocess
import os

#-----------import area ends ----------------------

# to open firefox webbroser and maximize the window 
browser = webdriver.Firefox()
browser.maximize_window()

#connect to the specific ip address
browser.get("enter the url where you want to login ")

#find the html text field names for input of name and password  
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

#fill the textfields with with the credentials 
username.send_keys("enter the username ")
password.send_keys("enter the password ")

#search the button in the html and click the submit button 
login = browser.find_element_by_name("btnSubmit")
login.submit()

#pause the execution of script for one second 
time.sleep(1)

#open chrome browser executable 
chrome = " enter chrome .exe file location "

#add all the websites you want to open in next tabs 
cmdline = [chrome]
cmdline.append("google.com")
cmdline.append("gmail.com")
cmdline.append("quora.com")
cmdline.append("geeksforgeeks.org")

#call the subprocess method and execute the command 
subprocess.Popen(cmdline)

#pause the script for three seconds  
time.sleep(3)

#open the editor used for the work 
os.startfile("enter the path to the editor you use often ")
