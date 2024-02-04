import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import time

Start_Time = time.time()

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(service=Service(), options=options)
driver.get("https://pixabay.com/gifs/")


divs = driver.find_elements(By.CLASS_NAME, "tags--lDvZS")
a_texts = []
for div in divs:
        for a in div.find_elements(By.TAG_NAME, 'a'):
            a_texts.append(a.get_attribute("textContent"))

def remove_duplicates(input_list):
    return list(set(input_list))

a_texts = remove_duplicates(a_texts)


for text in a_texts:
    os.makedirs(os.path.join(r"C:\Users\mobocomputer\Desktop\os\categories" , text),exist_ok=True)
    
a_hrefs = []
for div in divs:
        for a in div.find_elements(By.TAG_NAME, 'a'):
            a_hrefs.append(a.get_attribute("href"))
    

j = 0
for tag in a_texts:
    driver.get(a_hrefs[j])
    imgResults = driver.find_elements(By.CLASS_NAME, "image--FgLth")    
    i=1    
    imgs_Infos = [] 
    for img in imgResults:
        title = img.get_attribute('title')
        alt = img.get_attribute('alt')
        style = img.get_attribute('style')
        img_info = {'title':title, 'alt':alt, 'style':style}
        imgs_Infos.append(img_info)
        src = img.get_attribute('src')
        response = requests.get(src, stream=True)
        filename = os.path.join(r"C:\Users\mobocomputer\Desktop\os\categories",tag,f"gif_{i}.gif")  
        with open(filename, "wb") as out_file:
            out_file.write(response.content)
            print(f"gif_{i}.gif added to {tag}")      
        i+=1 
        
    for i in imgs_Infos:
        with open(os.path.join(r"C:\Users\mobocomputer\Desktop\os\categories",tag,f"{tag}.csv"), 'a', newline='') as csvfile:
            fieldnames = ['title', 'alt','style']
            writer = csv.DictWriter(csvfile,fieldnames=fieldnames) 
            writer.writerow(i)
        
    j+=1
    

End_Time   = time.time()
Total_Time = End_Time - Start_Time
print("total spending time: " , Total_Time)
