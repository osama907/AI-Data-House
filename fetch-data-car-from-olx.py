import requests
import pandas as pd
from bs4 import BeautifulSoup

titles = []
prices = []
links = []

for i in range(1, 6):
    url = f"https://usaolx.com/all-ads/listing-category/cars-vehicles/?page={i}"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")


    ads = soup.find_all("div", class_="rtcl-listing-item")

    for ad in ads:

        title_el = ad.find("h3")
        title = title_el.get_text()

        price_el = ad.find("span", class_="rtcl-price-amount amount")
        price = price_el.get_text(strip=True) if price_el else "N/A"

        link_el = ad.find("a", href=True)
        link = link_el["href"]

        titles.append(title)
        prices.append(price)
        links.append(link)

# Save to CSV
df = pd.DataFrame({"Title": titles, "Price": prices, "Link": links})
df.to_csv("carlist2.csv", index=False, encoding="utf-8")
