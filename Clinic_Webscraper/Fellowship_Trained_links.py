__author__ = 'gerson64'

#wget 'http://acms.execinc.com/edibo/SurgeonFinder/DetailsInset?'

import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL="http://acms.execinc.com/edibo/SurgeonFinder"

fileName = open("C:/Users/gerson64/Desktop/Dropbox Sync/Dropbox/Github/DirectoryScraper/Directory_Out/Fellow_Links.txt", 'w')



driver = webdriver.Firefox()
driver.get(URL)
time.sleep(5)

elem = driver.find_elements_by_id("ctl00_CphBody_tabContainer_tabPanel3_tab")
elem[0].click()
time.sleep(2)
elem = driver.find_elements_by_id("ctl00_CphBody_tabContainer_tabPanel3_BtnQuickSearch_DSI_QuickSearch")
elem[0].click()
#print(elem[0])

for x in range(1, 62):
#for x in range(1, 2):

    time.sleep(3)
    content = unicode(driver.page_source).lower()
#    print(content)
    regex= r'(http:\/\/acms\.execinc\.com\/edibo\/surgeonfinder\/detailsinset\?contactid=\d*)'
    matches = re.findall(regex,content)
    for match in matches:
        print(match)
        fileName.write(match+"\n")

    if x <> 62:
        element = WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.LINK_TEXT, str(x+1)))
        )
        elem = driver.find_elements_by_link_text(str(x+1))
        elem[0].click()
        time.sleep(2)

fileName.close()

