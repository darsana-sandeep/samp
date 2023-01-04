import requests
from bs4 import BeautifulSoup

wed_url = "https://xpayback.com/"

res = requests.get(wed_url)
soup =BeautifulSoup(res.text,"html5lib")

jobs = soup.find_all("div",{"class":"banner-content"})
#print(jobs)
for job in jobs:
    title_element = job.find("h1")
    print(title_element.text)



