from selenium import webdriver  #kütüphanelerin import edilmesi
import time                     
browser=webdriver.Firefox()     #browser olarak firefox tanımlanması

time.sleep(5) 

browser.get("https://www.instagram.com/")        #Urlye gitmesi
 
time.sleep(10)


username = browser.find_element("name", "username")          #username elementini sayfada arat ve usernameye ata
password = browser.find_element("name", "password")          #password elementini sayfada arat ve password ata


username.send_keys("kadirbulbulcom")                         #kullanıcı adınız
password.send_keys("parolamyok")                             #parolanız


#Burada ise sitede DOM kullanarak , xpath yolu verilen  elementi giris_yap değişkenine atıyoruz.

giris_yap=browser.find_element("xpath","/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]") 
giris_yap.click()  # Giriş yap değişkenine tıklansın

time.sleep(10)

browser.close()