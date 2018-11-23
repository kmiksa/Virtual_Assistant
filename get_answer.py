from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys



class Fetcher():
    def __init__(self,url):
        self.driver = webdriver.Chrome()
        self.driver.wait = WebDriverWait(self,5)
        self.url = url
        print(self.url)
        #self.lookup()


    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "gsfi")
            ))
        except:
            print("Failed")


        soup = BeautifulSoup(self.driver.page_source, "html.parser")

        if soup.find_all(class_="Z0LcW"):
            answer = soup.find_all(class_= "Z0LcW")
            return answer[0].get_text()

        elif soup.find_all(class_="cwcot gsrt"):
            answer = soup.find_all(class_="cwcot gsrt")
            return answer[0].get_text()

        else:
            return

