# COVID-19 TRACKER

from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="E:\corona.ico",  # Image(.ico) file location
        timeout=10  # seconds
    )


def getData(url):
    r = requests.get(url)
    return r.text


# while True:

myHtmlData = getData('https://www.mohfw.gov.in/')
# print(myHtmlData)
soup = BeautifulSoup(myHtmlData, 'html.parser')
# print(soup.prettify())
myDataStr = ""
for tr in soup.find_all('tbody')[1].find_all('tr'):
    myDataStr += tr.get_text()
myDataStr = myDataStr[1:]
itemList = (myDataStr.split("\n\n"))
states = ['Maharashtra', 'West Bengal', 'Kerala']
for item in itemList[0:23]:
    dataList = (item.split('\n'))
    if dataList[1] in states:
        print(dataList)
        nTitle = "Cases of Covid-19"
        nText = f"State :  {dataList[1]}\nIndians :  {dataList[2]}\nForeigners :  {dataList[3]}\nCured :  {dataList[4]}\nDeaths :  {dataList[5]}"
        notifyme(nTitle, nText)
        time.sleep(12)

# time.sleep(600)  #  After how many seconds you want to display the msg again
