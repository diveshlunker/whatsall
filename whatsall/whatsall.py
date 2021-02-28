from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import csv

location_driver = ""
def driver_check(location):
    driver_file = os.path.exists(location)
    if driver_file:
        global location_driver
        location_driver = location
        return True
    else:
        print("Download the Chrome driver exe file -> unzip it -> see the location -> continue.")
        return False

def startdriver(location = "c://drivers//chromeDriver//chromedriver.exe"):
    if(driver_check(location)):
        driver = webdriver.Chrome(executable_path=str(location))
        return driver
    else:
        print("Error while launching chrome!!")
        return None

def add_numbers(phone_numbers, country_code):
    contacts = []
    country_code = country_code.strip("")
    country_code = country_code.strip("+")
    country_code = country_code.strip("\n")
    
    for number in phone_numbers:
        number = number.strip("\n")
        number = number.strip("")
        number = str(country_code)+str(number)
        contacts.append(number)
        
    return contacts
        
def add_messages(message):
    messages = []
    messages = message
    
    return messages
    
def csv_numbers(csv_location, country_code = None):
    
    fields = [] 
    rows = [] 
    contacts = []

    with open(csv_location, 'r') as csvfile: 

        csvreader = csv.reader(csvfile) 
    
        for row in csvreader: 
            rows.append(row) 
  
    if (country_code):
         for i in range(len(rows)):
            if(i>0):
                
                phone_number = rows[i][0]

                phone_number = phone_number.strip(" ")
                phone_number = phone_number.strip("\n")
                phone_number = phone_number.strip("+")
                country_code = country_code.strip("+")
                country_code = country_code.strip(" ")
                country_code = country_code.strip("\n")

                contacts.append(str(country_code)+str(phone_number))
            
    else:
        
        for i in range(len(rows)):
            
            if(i>0):
                phone_number = rows[i][0]
                country_code = rows[i][1]

                phone_number = phone_number.strip(" ")
                phone_number = phone_number.strip("\n")
                phone_number = phone_number.strip("+")
                country_code = country_code.strip("+")
                country_code = country_code.strip(" ")
                country_code = country_code.strip("\n")

                contacts.append(str(country_code)+str(phone_number))
    
    return contacts

def messages_csv(csv_location):
    messages = []
    
    with open(csv_location, 'r') as csvfile: 

        csvreader = csv.reader(csvfile) 
    
        for row in csvreader: 
            messages.append(row)
    
    return messages

def send_message(phone_numbers = None, country_code = None, list_messages = None, csv_numbers_location = None, csv_messages_location = None, driver_location = None):
    
    if(phone_numbers and country_code):
        contacts = add_numbers(phone_numbers, country_code)
    if(list_messages):
        messages = add_messages(list_messages)
    if(csv_numbers_location and country_code):
        contacts = csv_numbers(csv_numbers_location, country_code)
    if(csv_numbers_location and not country_code):
        contacts = csv_numbers(csv_numbers_location)
    if(csv_messages_location):
        messages = messages_csv(csv_messages_location)
    if(driver_location):
        driver = startdriver(driver_location)
    else:
        driver = startdriver()
    
    if(len(contacts)>0 and len(messages)>0 and driver):
        
        driver.get("https://web.whatsapp.com/")
        time.sleep(15)
        for num in contacts:
            driver.get("https://web.whatsapp.com/send?phone="+str(num)+"&text&source&data&app_absent")
            time.sleep(10)
        
            try:
                input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

                shift_enter = ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER)
                for message in messages:
                    parts = message.split("\n")
                    for part in parts:
                        input_box.send_keys(part)
                        shift_enter.perform()
                    input_box.send_keys(Keys.ENTER)
                time.sleep(3)
            
            except:
                ok_button = driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div')
                ok_button.click()
                print("Message not successfully sent to",str(num))
                time.sleep(3)
                
                
def add_images(list_images):
    images = []
    for image in list_images:
        image.strip("\n")
        image.strip(" ")
        images.append(image)
    
    return images

def images_csv(csv_location):
    images = []
    
    with open(csv_location, 'r') as csvfile: 
        csvreader = csv.reader(csvfile) 
    
        for row in csvreader: 
            images.append(row)
    
    return images


def send_image(phone_numbers = None, country_code = None, list_images = None, csv_numbers_location = None, csv_images_location = None, driver_location = None):
       
    contacts = []
    images = []
    
    if(phone_numbers and country_code):
        contacts = add_numbers(phone_numbers, country_code)
    if(list_images):
        images = add_images(list_images)
    if(csv_numbers_location and country_code):
        contacts = csv_numbers(csv_numbers_location, country_code)
    if(csv_numbers_location and not country_code):
        contacts = csv_numbers(csv_numbers_location)
    if(csv_images_location):
        images = images_csv(csv_images_location)
    if(driver_location):
        driver = startdriver(driver_location)
    elif(driver_location==None):
        driver = startdriver()
    
    if(len(contacts)>0 and len(images)>0 and driver):
        
        driver.get("https://web.whatsapp.com/")
        time.sleep(15)
        
        for num in contacts:
            driver.get("https://web.whatsapp.com/send?phone="+str(num)+"&text&source&data&app_absent")
            time.sleep(10)
            
            try:
                for image_path in images:

                    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
                    attachment_box.click()

                    image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                    image_box.send_keys(image_path)

                    time.sleep(3)

                    send_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
                    send_button.click()
            except:
                ok_button = driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div')
                ok_button.click()
                print("Message not successfully sent to",str(num))
                time.sleep(3)

def add_docs(list_docs):
    documents = []
    for doc in list_docs:
        doc.strip("\n")
        doc.strip(" ")
        documents.append(doc)
    return documents

def docs_csv(csv_location):
    documents = []
    
    with open(csv_location, 'r') as csvfile: 
        csvreader = csv.reader(csvfile) 
    
        for row in csvreader: 
            documents.append(row)
    return documents


def send_documents(phone_numbers = None, country_code = None, list_documents = None, csv_numbers_location = None, csv_documents_location = None, driver_location = None):
    
    documents = []
    
    if(phone_numbers and country_code):
        contacts = add_numbers(phone_numbers, country_code)
    if(list_documents):
        documents = add_docs(list_documents)
    if(csv_numbers_location and country_code):
        contacts = csv_numbers(csv_numbers_location, country_code)
    if(csv_numbers_location and not country_code):
        contacts = csv_numbers(csv_numbers_location)
    if(csv_documents_location):
        documents = docs_csv(csv_documents_location)
    if(driver_location):
        driver = startdriver(driver_location)
    elif(driver_location==None):
        driver = startdriver()
    
    if(len(contacts)>0 and len(documents)>0 and driver):
        
        driver.get("https://web.whatsapp.com/")
        time.sleep(15)
        
        for num in contacts:
            driver.get("https://web.whatsapp.com/send?phone="+str(num)+"&text&source&data&app_absent")
            time.sleep(10)
            
            
            try:
                for doc_path in documents:

                    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
                    attachment_box.click()

                    image_box = driver.find_element_by_xpath('//input[@accept="*"]')
                    image_box.send_keys(doc_path)

                    time.sleep(3)

                    send_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')

                    send_button.click()
            except:
                ok_button = driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div')
                ok_button.click()
                print("Message not successfully sent to",str(num))
                time.sleep(3)

def send_customized_message(messages = None, csv_custom_messages_location = None, country_code = None, driver_location = None):
    
    fields = [] 
    rows = [] 
    
    if(driver_location):
        driver = startdriver(driver_location)
    else:
        driver = startdriver()
    
    driver.get("https://web.whatsapp.com/")
    time.sleep(15)
    
    with open(csv_custom_messages_location, 'r') as csvfile: 

        csvreader = csv.reader(csvfile) 
    
        for row in csvreader: 
            rows.append(row)
        
        if(country_code):
            header = rows[0]
            print(header)
            s = ""
            for i in range(len(rows)):
                if(i>0):
                    num = rows[i][0]
                    num = country_code+num
                    s = ""
                    for message in messages:
                        modified_message = message.split(" ")
                        for j in range(len(header)):
                            if(j>0):
                                if("%"+str(header[j])+"%" in modified_message):
                                    
                                    for item_position in range(len(modified_message)):
                                        if(modified_message[item_position]=="%"+str(header[j])+"%"):
                                            modified_message[item_position] = rows[i][j]
                                    
                                    
                        modified_message = " ".join(modified_message)                        
                        
                        driver.get("https://web.whatsapp.com/send?phone="+str(num)+"&text&source&data&app_absent")
                        time.sleep(10)
                        
                        try:
                            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

                            shift_enter = ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER)

                            parts = modified_message.split("\n")
                            for part in parts:
                                input_box.send_keys(part)
                                shift_enter.perform()
                            input_box.send_keys(Keys.ENTER)
                            time.sleep(3)
                        
                        except:
                            ok_button = driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div')
                            ok_button.click()
                            print("Message not successfully sent to",str(num))
                            time.sleep(3)
                            
send_message(phone_numbers=["9884"],country_code = "91", list_messages=["hello","here i am"])
