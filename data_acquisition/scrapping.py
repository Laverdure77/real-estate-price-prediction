import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import data_filter

def immoweb_scrapping(url):

    my_dict = dict()

    tab = url.split("/")
    my_dict["Locality"] = tab[7].capitalize()
    my_dict["Type of property"] = tab[5]
    my_dict["Type of sale"] = tab[6]

    driver = webdriver.Chrome()
    driver.get(url)

    for key, value in zip(driver.find_elements(By.XPATH, "//th"), driver.find_elements(By.XPATH, "//td")):
        my_dict[key.text.replace("\n", "")] = value.text.replace("\n", "")

    driver.close()

    return data_filter.immoweb_filter(my_dict)

print(immoweb_scrapping("https://www.immoweb.be/fr/annonce/maison/a-vendre/deinze/9800/10304762"))
print(immoweb_scrapping("https://www.immoweb.be/fr/annonce/maison/a-vendre/juprelle/4451/10277587"))