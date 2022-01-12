import requests
from bs4 import BeautifulSoup

resp = requests.get(f"http://www.srikanthtechnologies.com")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit(1)

bs = BeautifulSoup(resp.text, 'html.parser')
links = bs.find_all('a')
for a in links:
    print(a['href'])
