import requests
from bs4 import BeautifulSoup

WEBSITE = "https://www.khanacademy.org"
resp = requests.get(WEBSITE)
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit(1)

bs = BeautifulSoup(resp.text, 'html.parser')
links = bs.find_all('a')
for a in links:
    if 'href' not in a.attrs:
        continue

    href = a["href"]
    if href == "#":
        continue
    if not href.startswith("http"):
        if href.startswith("/"):
            href = WEBSITE + href
        else:
            href = WEBSITE + "/" + href

    print(href)
