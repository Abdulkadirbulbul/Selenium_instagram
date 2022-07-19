#kütüphanelerin import edilmesi
from selenium import webdriver  
import time                     
import json

#kullanıcıadı ve şifremi json dosyasından alıyorum.
jsonFile = open('./secret.json') 
jsonData = json.load(jsonFile)   


#browser olarak firefox tanımlanması
browser=webdriver.Firefox()    


time.sleep(5) 

#Urlye gitmesi
browser.get("https://www.instagram.com/")        
 
time.sleep(5)

 #username elementini sayfada arat ve usernameye ata
username = browser.find_element("name", "username")   

 #password elementini sayfada arat ve password ata    
password = browser.find_element("name", "password")         

 #kullanıcı adınız
username.send_keys(jsonData['username']) 
 #parolanız                       
password.send_keys(jsonData['password'])                            


#Burada ise sitede DOM kullanarak , xpath yolu verilen  elementi giris_yap değişkenine atıyoruz.

giris_yap=browser.find_element("xpath","/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]") 
# Giriş yap değişkenine tıklansın

giris_yap.click()  
time.sleep(10)

browser.close()