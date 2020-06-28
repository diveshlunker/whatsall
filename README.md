# whatsAll
WhatsAll is a Python library to automate sending messages to unlimited number of people without even saving the contact number.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install whatsall
```bash
pip install whatsall
```
## Requirements
- Python 3 - Download it [here](https://www.python.org/downloads/)
- Google chrome driver - Download the driver [here](https://chromedriver.chromium.org/downloads). Unzip and place the google driver at this location:- __C:\Drivers\chromeDriver\chromedriver.exe__ for easy use of the library
- selenium library - install by 
```bash
pip install selenium
```
- Check the other basic libraries from [requirements.txt](https://github.com/diveshlunker/whatsall/blob/master/requirements.txt) which should be generally pre installed but in case it isn't, install it.

## Features
- Automate messaging to unlimited users.
- No need to save the contact in order to message the user.
- Send messages to people of any country just by specifying the country code.
- You can add multiple messages.

## Features to be added
- Enabling media and document share to people.
- Instead of a list as parameter for messages and contact numbers, reading different documents and retreiving the numbers.
- Handling errors in case the internet is slow or the number is invalid.

## Usage
```python
import whatsall.whatsall as whatsall

whatsall.helpdesk()
```
Calling helpdesk will list you all the features of the library and the detail flow of each function.
```bash
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
    
    6. send_message() - Will start sending messages
    
    7. speed(time_in_seconds) - send time in seconds - increase if your internet is slow in order to send message properly.
    
    8. stop() - use this function to stop messaging and close the chrome driver
    
    ------------------------------------------------------------------------------------------------------------------------
    
    Additional Functionality will be added soon.
    Feel free to contribute to the library.
    
    Contact developer @:-
        Gmail - ndiveshjain@gmail.com
        Github - @diveshlunker
        Linkedin - @divesh-jain-652973145
    
    
```

## Sample Code

```python

import whatsall.whatsall as whatsall
whatsall.start()
whatsall.numbers([98845*****,86456*****],91) #add as many numbers as you want in list
whatsall.message(["Hey, Divesh here, just wanted to ask if whatsall worked properly?"]) #add as many messages as you wish in the list
whatsall.send_message()

```

## Terms and Conditions
- This library is unofficial and is no way responsible for any legal issues if happen.
- This library should not be used for any illeagal purpose and is made merely for education purpose and for development.
- For any major changes, issue must be raised first.
- This library should not be used for spamming else, if blocked by whatsapp, this library should not be held responsible


## Contributing
Pull requests are welcome. 
Thanks [Codenomous](https://codenomous.wordpress.com/2020/06/28/whatsall-whatsapp-sutomation-bulk/) for writing a blog on my library and infact starting your blog with my library.

## Version
Stable version - 1.1.1

## License
[MIT](https://github.com/diveshlunker/whatsall/blob/master/LICENSE)
