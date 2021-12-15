import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
    "Accept-Language": "en-US,en;q=0.5",
}


def identify_website(url):
    split_url = url.split("/")
    website_name = split_url[2]
    return website_name


def get_price(url):
    website = identify_website(url)
    if website == "www.flipkart.com":
        price = find_price_flipkart(url)
    elif website == "www.amazon.in":
        price = find_price_amazon(url)
    else:
        price = "invalid link"
    return price


def find_price_flipkart(url):
    response = requests.get(url=url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "lxml")
    try:
        price = float(soup.find(class_="_30jeq3").getText().split("₹")[1].replace(",", ""))
    except:
        price = "Unable to retrieve"
    return price


def find_price_amazon(url):
    response = requests.get(url=url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "lxml")
    try:
        price = float(soup.find(id="price_inside_buybox").getText().split("₹")[1].replace(",", ""))
        # price = float(soup.find(id ="priceblock_ourprice").getText().split("₹")[1].replace(",", ""))
    except:
        price = "Unable to retrieve"
    return price


def price_dropped(unit_price, desired_price):
    if unit_price < desired_price:
        return True
