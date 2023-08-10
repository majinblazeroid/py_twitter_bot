from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

DOWN_SPEED = 100
UP_SPEED = 100
TWITTER_EMAIL ="TWITTER EMAIL ID"
TWITTER_PASS ="TWITTER PASSWORD"
HATHWAY = "INTERNET SERVICE PROVIDER"
W=3

class InternetSpeedTwitterBot():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self)-> tuple:
        self.driver.get("https://www.speedtest.net/")
        button = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        button.click()
        sleep(40)
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.driver.close()

    def tweet_at_provider(self):
        if UP_SPEED > self.up or DOWN_SPEED> self.down:
            tweet = f"Dear {HATHWAY} why is the speed down:{self.down}/up:{self.up}Mbps while I was promised 100Mbps"
            self.driver.get("https://twitter.com/i/flow/login")
            sleep(10)
            username = self.driver.find_element(By.CSS_SELECTOR, '.r-30o5oe')
            username.send_keys(TWITTER_EMAIL)
            sleep(W)
            username.send_keys(Keys.ENTER)
            sleep(W)
            try:
                user = self.driver.find_element(By.NAME, 'text')
                user.send_keys("MenkaSG")
                sleep(W)
                user.send_keys(Keys.ENTER)
            except NoSuchElementException:
                pass
            finally:
                sleep(W)
                passw = self.driver.find_element(By.NAME, "password")
                passw.send_keys(TWITTER_PASS)
                passw.send_keys(Keys.ENTER)

            # add tweet
            sleep(6)
            tweet_box = self.driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-ltr ")
            tweet_box.send_keys(tweet)
        else :
            print("You gettin good speeds babe")
        self.driver.close()





#box xpaath =/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div
#share xpath = /html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div
#/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input


#//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input