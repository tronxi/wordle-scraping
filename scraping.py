from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

web = "https://www.wordmine.info/Search?stype=words-with&slang=es&sword=&letters=on&minletters=5&maxletters=5"
file = open("words.txt", "a")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(web)
div_words = driver.find_elements(By.CLASS_NAME, "foundword")
for word in div_words:
    childWord = word.find_element(By.TAG_NAME, "a").text + "\n"
    file.write(childWord)

for i in range(125):
    next = driver.find_element(By.LINK_TEXT, "Next").click()
    time.sleep(2)
    div_words = driver.find_elements(By.CLASS_NAME, "foundword")
    for word in div_words:
        childWord = word.find_element(By.TAG_NAME, "a").text + "\n"
        file.write(childWord)
file.close()
driver.close()