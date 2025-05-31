import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_bbc():
    url = "https://www.bbc.com/news"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print("Failed to fetch BBC news.")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    headlines = [
        tag.get_text(strip=True)
        for tag in soup.find_all("h2", class_="sc-9d830f2a-3 fWzToZ")
        if len(tag.get_text(strip=True)) > 20
    ]
    return headlines[:10]

def scrape_cnn():
    url = "https://edition.cnn.com/world"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print("Failed to fetch CNN news.")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    headlines = [
        tag.get_text(strip=True)
        for tag in soup.find_all("span", class_="container__headline-text")
        if len(tag.get_text(strip=True)) > 20
    ]
    return headlines[:10]
