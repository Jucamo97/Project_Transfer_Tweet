#Library
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import tweepy
import time
from seleniumbase import Driver

# #Driver Settings
# options = webdriver.ChromeOptions()
# options.add_argument('--start-maximized')
# options.add_argument("--headless")
# options.add_argument('--disable-extensions')
# options.add_argument("--disable-dev-shm-usage");
# options.add_argument("--disable-renderer-backgrounding");
# options.add_argument("--disable-background-timer-throttling");
# options.add_argument("--disable-backgrounding-occluded-windows");
# options.add_argument("--disable-client-side-phishing-detection");
# options.add_argument("--disable-crash-reporter");
# options.add_argument("--disable-oopr-debug-crash-dump");
# options.add_argument("--no-crash-upload");
# options.add_argument("--disable-gpu");
# options.add_argument("--disable-extensions");
# options.add_argument("--disable-low-res-tiling");
# options.add_experimental_option('excludeSwitches', ['enable-logging'])

#driver = webdriver.Chrome(options= options)

driver = Driver(uc=True,headless=True)
driver.get('https://www.transfermarkt.co/liga-dimayor-apertura/letztetransfers/wettbewerb/COLP/plus/1')

time.sleep(8)

#Accept Cookies
iFrame = driver.find_element(By.ID,'sp_message_iframe_953420')
driver.switch_to.frame(iFrame)
cookie = driver.find_element(By.XPATH,'//*[@id="notice"]/div[3]/div[1]/div/button').click()
driver.switch_to.default_content()

#Scrap data
def get_data():
    mainTable = []
    for x in range(1,7):
        namePlayer = driver.find_element(By.XPATH,f'//*[@id="yw1"]/table/tbody/tr[{x}]/td[1]/table/tbody/tr[1]/td[2]/a').text
        agePlayer = driver.find_element(By.XPATH,f'//*[@id="yw1"]/table/tbody/tr[{x}]/td[3]').text
        lastTeamPlayer = driver.find_element(By.XPATH,f'//*[@id="yw1"]/table/tbody/tr[{x}]/td[4]/table/tbody/tr[1]/td[2]/a').text
        newTeamPlayer = driver.find_element(By.XPATH,f'//*[@id="yw1"]/table/tbody/tr[{x}]/td[5]/table/tbody/tr[1]/td[2]/a').text
        datePlayer = driver.find_element(By.XPATH,f'//*[@id="yw1"]/table/tbody/tr[{x}]/td[6]').text
        transferValuePlayer = driver.find_element(By.XPATH,f'//*[@id="yw1"]/table/tbody/tr[{x}]/td[7]').text

        rowTable = {}
        rowTable['Player_Name'] = namePlayer
        rowTable['Player_Age'] = int(agePlayer)
        rowTable['Last_Team'] = lastTeamPlayer
        rowTable['New_Team'] = newTeamPlayer
        rowTable['Date'] = datePlayer
        rowTable['Transfer_Value'] = transferValuePlayer
        
        mainTable.append(rowTable)
        print(namePlayer,agePlayer,lastTeamPlayer,newTeamPlayer,datePlayer,transferValuePlayer)

    return mainTable

data = get_data()

#Checker
Tweet = []

temporal = pd.read_csv('Project_Transfer_Tweet/initial.csv')
temporal = temporal.to_dict(orient='records')

for x in data:
    if x not in temporal:
        temporal.append(x)
        Tweet.append(x)
    else:
        print('Record already exists')

temporal = pd.DataFrame(temporal)
temporal.to_csv('Project_Transfer_Tweet/initial.csv',index=False)

#Check if there are tweets
if len(Tweet) > 0:
    tweetTable = pd.DataFrame(Tweet)

    for x in range(len(tweetTable.index)):

        Name = tweetTable.iloc[x]['Player_Name'] 
        Age = tweetTable.iloc[x]['Player_Age']
        New_Team = tweetTable.iloc[x]['New_Team']
        Last_Team = tweetTable.iloc[x]['Last_Team']
        Transfer = tweetTable.iloc[x]['Transfer_Value']

        if Transfer == 'Libre':
            Tweet = f'{Name} de {Age} años es nuevo jugador de {New_Team}, llega como Agente Libre. Su equipo anterior fue {Last_Team}.'
            print(Tweet)

        elif Transfer == '?':
            Tweet = f'{Name} de {Age} años es nuevo jugador de {New_Team}, su equipo anterior fue {Last_Team}.'
            print(Tweet)
        
        elif Transfer == '-':
            Tweet = f'{Name} de {Age} años es ahora Agente Libre, su equipo anterior fue {Last_Team}.'
            print(Tweet)

        else:
            Tweet = f'{Name} de {Age} años es nuevo jugador de {New_Team}. Compra por valor de {Transfer}.'
            print(Tweet)


            #Tweepy Settings
        api_key = "KDUGgujyObm2cK0d0ckiDjkUT"
        api_secret = "89OkMWycXZQRsH9961Yu7YeZK6wLizLgSey1WanPqMIqfgw82R"
        bearer_token = r"AAAAAAAAAAAAAAAAAAAAANEtrwEAAAAAYk%2FVyGlB97XFu7q5psrriG0Z3p0%3DIvsHejuxkyMjLE9HsFE9ydLSKm3OxlQGYfrbyxSxY0IirtG9Sc"
        access_token = "1743376837969838080-gbBNkHtJokKWsKlr3hlMxb6y1La5DI"
        access_token_secret = "lNM88hqq4Yt4PcxYRF46MxFDUZ9VWdKNP2rHB33PQwN2K"

        client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
        client.create_tweet(text=Tweet)
            
else:
    print('No news')

driver.quit()