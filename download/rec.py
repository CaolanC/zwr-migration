import requests
from bs4 import BeautifulSoup
import os

b_url = 'https://zwr.gg/'

def grabJSON(soup, url):

    jsons = soup.find_all("script", {"type":"application/json"}, id=True)
    os.makedirs(url, exist_ok=True)
    for json in jsons:

        with open(url + "/" + json['id'] + ".json", "w") as f:
            f.write("".join(json.contents))
            print(f'Records saved as {url}/{json["id"]}.json')

visited = []

def recLinks(url=b_url):

    r = requests.get(url)
    if not r.status_code == 200:

        print(url, r.status_code)
        return

    soup = BeautifulSoup(r.text, 'lxml')
    body = soup.find("div", {"class":'page-contents'})
    links = body.find_all("a", href=True, title=False, rel=False)

    if soup.find("div", {"class":"SubBoards"}):

        grabJSON(soup, url)

    else:

        for link in links:
            if 'class' in link:

                printf('class: {link["class"]}')
                return

            href = link['href']
        
            if not href in visited:
                visited.append(href) 
                print(url + href[1:])
                recLinks(b_url + href[1:])

recLinks(b_url + "leaderboards")
