import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_amazon():
    url = "https://www.amazon.in/s?k=laptops"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for item in soup.select('.s-result-item'):
        title = item.select_one('h2').get_text(strip=True) if item.select_one('h2') else None
        price = item.select_one('.a-price-whole').get_text(strip=True) if item.select_one('.a-price-whole') else None
        discount = item.select_one('.a-badge-text').get_text(strip=True) if item.select_one('.a-badge-text') else None
        rating = item.select_one('.a-icon-alt').get_text(strip=True) if item.select_one('.a-icon-alt') else None
        products.append([title, price, discount, "Amazon", rating])

    return pd.DataFrame(products, columns=['Product', 'Price', 'Discount', 'Platform', 'Rating'])

if __name__ == "__main__":
    amazon_data = scrape_amazon()
    amazon_data.to_csv('data/laptops_data.csv', mode='a', header=False, index=False)
