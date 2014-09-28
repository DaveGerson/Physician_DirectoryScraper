__author__ = 'gerson64'


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


html_for_input = "www.mohssurgery.org/i4a/member_directory/feResultsListing.cfm?directory_id=3&bAdminPopup=0&viewAll=0"
html_for_input = "http://" + html_for_input

fileName = open("C:/Users/gersonda/Dropbox/Github/DirectoryScraper/Directory_Out/Non_Fellow_Links.txt", 'w')



driver = webdriver.Firefox()
driver.get(html_for_input)


for x in range(1, 47):
#for x in range(1, 2):
    element = WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "View Details"))
    )
    details = driver.find_elements_by_partial_link_text("View Details")
    for detail in details:
        print(detail)
        fileName.write(detail.get_attribute("href")+"\n")
    element = WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Next "))
    )
    elem = driver.find_elements_by_partial_link_text("Next ")
    elem[0].click()
    print(elem[0])

fileName.close()

