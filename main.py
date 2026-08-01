import time
import logging
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

BASE_URL = "http://books.toscrape.com/catalogue/"
START_URL = "http://books.toscrape.com/catalogue/page-1.html"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def parse_book_card(book):
    title = book.h3.a["title"].strip()
    
    # Extract only the numerical price using regex (handles Â£, £, $, etc.)
    raw_price = book.find("p", class_="price_color").text
    price_match = re.search(r"[\d.]+", raw_price)
    price = float(price_match.group()) if price_match else 0.0
    
    instock = "In stock" in book.find("p", class_="instock availability").text
    
    rating_cls = book.find("p", class_="star-rating")["class"]
    rating_str = [c for c in rating_cls if c != "star-rating"][0]
    rating = RATING_MAP.get(rating_str, 0)
    
    relative_link = book.h3.a["href"]
    product_url = BASE_URL + relative_link.replace("catalogue/", "")

    return {
        "Title": title,
        "Price (£)": price,
        "Rating (1-5)": rating,
        "In Stock": instock,
        "URL": product_url
    }

def scrape_catalog(max_pages=5):
    current_url = START_URL
    scraped_books = []
    page_count = 1

    session = requests.Session()
    session.headers.update(HEADERS)

    while current_url and page_count <= max_pages:
        logging.info(f"Fetching page {page_count}: {current_url}")
        
        try:
            resp = session.get(current_url, timeout=10)
            if resp.status_code != 200:
                logging.warning(f"Failed to fetch page {page_count}. Status: {resp.status_code}")
                break

            soup = BeautifulSoup(resp.text, "html.parser")
            book_cards = soup.find_all("article", class_="product_pod")
            
            for card in book_cards:
                data = parse_book_card(card)
                scraped_books.append(data)

            next_btn = soup.find("li", class_="next")
            if next_btn and next_btn.a:
                next_page = next_btn.a["href"]
                current_url = BASE_URL + next_page if "catalogue/" not in next_page else "http://books.toscrape.com/" + next_page
                page_count += 1
                time.sleep(1)
            else:
                current_url = None

        except Exception as err:
            logging.error(f"Error scraping {current_url}: {err}")
            break

    return scraped_books

def export_to_excel(records, filename="scraped_books_output.xlsx"):
    if not records:
        logging.warning("No data to save.")
        return

    df = pd.DataFrame(records)
    
    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Books")
        
    logging.info(f"Successfully saved {len(df)} rows to '{filename}'.")

if __name__ =="__main__":
    logging.info("Starting Web Scraping Job...")
    results = scrape_catalog(max_pages=5)
    export_to_excel(results)
    logging.info("Scraping task completed.")
