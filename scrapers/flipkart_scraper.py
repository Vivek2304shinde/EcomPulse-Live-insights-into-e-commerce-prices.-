import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart():
    url = "https://www.flipkart.com/search?q=laptops"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for item in soup.select('._1AtVbE'):
        title = item.select_one('._4rR01T').get_text(strip=True) if item.select_one('._4rR01T') else None
        price = item.select_one('._30jeq3').get_text(strip=True) if item.select_one('._30jeq3') else None
        discount = item.select_one('._3Ay6Sb').get_text(strip=True) if item.select_one('._3Ay6Sb') else None
        rating = item.select_one('._3LWZlK').get_text(strip=True) if item.select_one('._3LWZlK') else None
        products.append([title, price, discount, "Flipkart", rating])

    return pd.DataFrame(products, columns=['Product', 'Price', 'Discount', 'Platform', 'Rating'])

if __name__ == "__main__":
    flipkart_data = scrape_flipkart()
    flipkart_data.to_csv('data/laptops_data.csv', mode='a', header=False, index=False)
