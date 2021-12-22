from selenium import webdriver
from selenium.webdriver.common import by
import time
import os
from easygui import msgbox

class crawlWebsite:

    def loadDriver(self,url,pth):
        driver=webdriver.Chrome()
        driver.implicitly_wait(7)
        driver.maximize_window()
        driver.get(url)
        element=driver.find_element(by='xpath',value="//div[@class='menu-wrapper']//input")
        self.uploadFile(element,pth)       

    def uploadFile(self,element,pth):
        element.send_keys(pth)
        time.sleep(3)
        msgbox("File uploaded successfully..", title="File Upload.")


if __name__ == '__main__': 
    cw=crawlWebsite()
    url = 'https://convertio.co/'
    pth=input("Please enter completer path of file to upload.")    
    if os.path.exists(pth):
        cw.loadDriver(url,pth)    
    else:
        msgbox("Please select the correct path..",title="Path Error..")    





