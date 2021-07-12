import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/0321751043/?coliid=I2L8XLS6K64D6Q&colid=3MPUEYS166452&psc=1&ref_=lv_ov_lig_dp_it"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, lxml)
print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)