from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

import time

driver = webdriver.Chrome()

driver.get("https://opstra.definedge.com/")

driver.maximize_window()

time.sleep(2)

element = driver.find_element(By.CSS_SELECTOR, "#app > div.application--wrap > nav > div > div:nth-child(5) > button")
element.send_keys(Keys.RETURN)

time.sleep(2)

element = driver.find_element(By.CSS_SELECTOR, "#username")
element.send_keys("innitonuthirani@gmail.com")

element = driver.find_element(By.CSS_SELECTOR, "#password")
element.send_keys("123456789")

element = driver.find_element(By.CSS_SELECTOR, "#kc-login")
element.send_keys(Keys.RETURN)

time.sleep(2)

element = driver.find_element(By.CSS_SELECTOR, "#app > div.application--wrap > nav > div > div:nth-child(4) > a:nth-child(2)")
element.send_keys(Keys.RETURN)

time.sleep(2)

element = driver.find_element(By.CSS_SELECTOR, "#app > div.application--wrap > main > div > div > div > div > div.home > div.container > div.v-card.v-card--flat.v-sheet.theme--light > div:nth-child(5) > div:nth-child(1) > div > div > div.v-input__slot > div.v-select__slot > input[type=text]")
element.send_keys(Keys.RETURN)
element.send_keys(Keys.DOWN)
element.send_keys(Keys.DOWN)
element.send_keys(Keys.RETURN)
time.sleep(2)


element = driver.find_element(By.CSS_SELECTOR, "#app > div.application--wrap > main > div > div > div > div > div.home > div.container > div.layout > ul > li")
element.send_keys(Keys.RETURN)

time.sleep(5)

#PHASE 2
j = 1
df_data = {}
names = []
for j in range(11):


    element = driver.find_element(By.CSS_SELECTOR, "#app > div.application--wrap > main > div > div > div > div > div.home > div.container > div.v-card.v-card--flat.v-sheet.theme--light > div:nth-child(5) > div:nth-child(2) > div > div > div.v-input__slot > div.v-select__slot > input[type=text]")
    element.send_keys(Keys.RETURN)
    time.sleep(1)
    k = 1
    for k in range(j):
        element.send_keys(Keys.DOWN)
        k = k+1
        time.sleep(0.1)
    element.send_keys(Keys.RETURN)
    Naam = driver.find_elements(By.XPATH, "//*/div[17]/div/div/div")
    time.sleep(1)
    CallLTP = driver.find_elements(By.XPATH, "//tbody/tr/td[1]/div")
    ITM_Prob = driver.find_elements(By.XPATH, "//tbody/tr/td[2]")
    CallIV = driver.find_elements(By.XPATH, "//tbody/tr/td[3]")
    CallDelta = driver.find_elements(By.XPATH, "//tbody/tr/td[4]")
    StrikePrice = driver.find_elements(By.XPATH, "//tbody/tr/td[5]")
    PutDelta = driver.find_elements(By.XPATH, "//tbody/tr/td[6]")
    PutIV = driver.find_elements(By.XPATH, "//tbody/tr/td[7]")
    ITM_Prob2 = driver.find_elements(By.XPATH, "//tbody/tr/td[8]")
    PutLTP = driver.find_elements(By.XPATH, "//tbody/tr/td[9]/div")

    time.sleep(1)


    table = []

    for i in range(len(StrikePrice)):
        temp={'CallLTP': CallLTP[i].text,
              'ITM Prob.': ITM_Prob[i].text,
              'CallIV': CallIV[i].text,
              'CallDelta': CallDelta[i].text,
              'Strike Price': StrikePrice[i].text,
              'Put Delta': PutDelta[i].text,
              'PutIV': PutIV[i].text,
              'ITM Prob.': ITM_Prob2[i].text,
              'PutLTP': PutLTP[i].text}
        table.append(temp)



    df_data_temp = pd.DataFrame(table)
    df_data[j] = df_data_temp


time.sleep(5)


df_data[1].to_csv("Assn4 Data1.csv")
df_data[2].to_csv("Assn4Data2.csv")
df_data[3].to_csv("Assn4 Data3.csv")
df_data[4].to_csv("Assn4 Data4.csv")
df_data[5].to_csv("Assn4 Data5.csv")
df_data[6].to_csv("Assn4 Data6.csv")
df_data[7].to_csv("Assn4 Data7.csv")
df_data[8].to_csv("Assn4 Data8.csv")
df_data[9].to_csv("Assn4 Data9.csv")
df_data[10].to_csv("Assn4Data10.csv")
