location = "C:\Drivers\chromeDriver\chromedriver.exe"
ini_time = 5
total_check = False
messages=[]
contacts = []
munum = "0"
country_code = "91"
driver="" 
c=1

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

def requirements_check(l):
    global c
    try:
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        import time
        import os
        return(1)
    except:
        print("Install all the required libraries using 'pip install -r requirements.txt'")
        return(0)

def driver_check(s):
    my_file = os.path.exists(s)
    if my_file:
        return True
    else:
        print("Download the Chrome driver exe file -> unzip it -> see the location -> continue.")

def startdriver(location):
    global driver
    driver = webdriver.Chrome(executable_path=str(location))

    
def total_check(diff_location):
    global location
    location = diff_location
    check = requirements_check(["time","os","sys","selenium","urllib","pathlib"])
    if(check==0):
        print("Thank you!")
    else:
        check2 = driver_check(location)
        if(check2):
            startdriver(location)
        else:
            print("Download the Chrome driver exe file and unzip it and save it and then continue.")
    
        if(check==1 and check2):
            return True
    

def start(diff_location="C:\Drivers\chromeDriver\chromedriver.exe"):
    global total_check
    total_check = total_check(diff_location)


        
def helpdesk(self):
    print("-------------------------------------------------------------------------")
    print("Welcome to Whatsapp Automated Messaging Library - WhatsAll")
    print("Developed by Divesh Lunker")
    print("Contribute @diveshlunker/whatsall on github")
    print("-------------------------------------------------------------------------")
    print("This library is totally unofficial and use it totally at your own risk")
    print("We do not take any responsibility for anything if goes wrong")
    print("--------------------------------------------------------------------------")
    print(""" 
    Follow the below instructions for easy use of this library
    
    1. start([location of chrome driver]) - use this function to start whatsall - If all the libraries are properly
                                            installed, you can proceed further. The parameter is optional. 
                                            The default location of driver is:- C:\Drivers\chromeDriver\chromedriver.exe
                                            If you save the driver in the particular location, sending location of driver 
                                            each time won't be required.
    
    2. startWeb(number,country_code) - send the number from which you wish to send for a trial purpose.
    
    3. message(list_message) - Use this function in order to set the message to be sent.
                               A list should be sent containing the message with each value 
                               in list depicting a new line of message
    
    4. numbers(list_numbers,country_code) - send the list of numbers whom you wish to send message with country_code
                                            as second parameter
                                            
    5. number(number,country_code) - Instead of list, individual number can be sent.
    
    6. speed(time_in_seconds) - send time in seconds - increase if your internet is slow in order to send message properly.
    
    7. stop() - use this function to stop messaging and close the chrome driver
    
    ------------------------------------------------------------------------------------------------------------------------
    
    Additional Functionality will be added soon.
    Feel free to contribute to the library.
    
    Contact developer @:-
        Gmail - ndiveshjain@gmail.com
        Github - @diveshlunker
        Linkedin - @divesh-jain-652973145
    
    """)
    
def message(list_message):
    if(total_check):
        global messages
        messages = list_message
    else:
        print("Please start the library before executing further commands. Thank you:)")
    
def send_message():
    if(total_check):
        global contacts
        global messages
        global ini_time
        ini_time = 20
        for i in contacts:
            print("https://web.whatsapp.com/send?phone="+str(i)+"&text&source&data&app_absent")
            driver.get("https://web.whatsapp.com/send?phone="+str(i)+"&text&source&data&app_absent")
            time.sleep(ini_time)
            ini_time = 5
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            for j in messages:
                input_box.send_keys(j)
                input_box.send_keys(Keys.ENTER)
            time.sleep(3)
    else:
        print("Please start the library before executing further commands. Thank you:)")
        
        
    
def numbers(list_numbers,countrycode):
    if(total_check):
        global contacts
        for i in list_numbers:
            i=str(i)
            i=i.strip()
            i = str(i)
            countrycode2 = str(countrycode)
            countrycode2 = countrycode2.strip("+")
            i = countrycode2+i
            contacts.append(i)
    else:
        print("Please start the library before executing further commands. Thank you:)")
    
def number(number,countrycode):
    if(total_check):
        global contacts
        countrycode2 = str(countrycode)
        countrycode2.strip("+")
        num = str(number)
        num = num.strip()
        num = countrycode+num
        contacts.append(num)
    else:
        print("Please start the library before executing further commands. Thank you:)")
        
def speed(time):
    if(total_check):
        global ini_time
        ini_time = time
    else:
        print("Please start the library before executing further commands. Thank you:)")
        
def startWeb(number,countrycode):
    if(total_check):
        global country_code
        global mynum
        global contacts
        country_code = countrycode
        mynum = number
        country_code = str(country_code)
        country_code.strip("+")
        mynum = str(mynum)
        mynum = country_code+mynum
        contacts.append(mynum)
    else:
        print("Please start the library before executing further commands. Thank you:)")

def stop():
    global driver
    global total_check
    driver.close()
    total_check = False

