"""
Broadband Plans Web Scraper
--------------------------
This script scrapes broadband plan information from findplanking.com using Selenium and BeautifulSoup4.
It extracts plan details including titles, descriptions, pricing, and contact information,
then saves the data in multiple formats (CSV, JSON, and TXT).

Requirements:
- Python 3.6+
- Selenium
- BeautifulSoup4
- ChromeDriver

Author: Your Name
License: MIT
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import csv
import json
from concurrent.futures import ThreadPoolExecutor

# Configuration Constants
CHROMEDRIVER_PATH = r"C:\Browserdrivers\chromedriver.exe"
BASE_URL = "https://findplanking.com"
MAIN_URL = f"{BASE_URL}/broadband"
MAX_WORKERS = 5  # Number of concurrent threads for scraping
LOAD_DELAY = 3   # Seconds to wait for JavaScript content to load

def get_page_content(url):
    """
    Fetch and parse HTML content using Selenium in headless mode.
    
    Args:
        url (str): The URL to fetch content from
        
    Returns:
        BeautifulSoup: Parsed HTML content
    """
    service = Service(CHROMEDRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(LOAD_DELAY)  # Wait for JavaScript to load content
        page_source = driver.page_source
    finally:
        driver.quit()

    return BeautifulSoup(page_source, 'html.parser')

def scrape_links(soup):
    """
    Extract all broadband plan links from the main page.
    
    Args:
        soup (BeautifulSoup): Parsed HTML content of the main page
        
    Returns:
        list: List of URLs for individual plan pages
    """
    section = soup.find("div", class_="listview_list__o3jbr")
    if not section:
        print("Warning: Main section not found!")
        return []
        
    links = section.find_all("a", href=True)
    plan_urls = [BASE_URL + link['href'] for link in links if "/broadband/" in link['href']]
    return plan_urls

def scrape_plan_details(url):
    """
    Scrape plan details from individual plan pages.
    
    Args:
        url (str): URL of the plan page to scrape
        
    Returns:
        dict: Dictionary containing plan details or None if scraping fails
    """
    soup = get_page_content(url)
    if not soup:
        return None
        
    details = {}

    # Extract plan components with error handling
    try:
        title_tag = soup.find("div", class_="plan_title__EaKQd")
        details['Title'] = title_tag.text.strip() if title_tag else "N/A"

        description_tag = soup.find("div", class_="plan_ul__zhREz")
        details['Description'] = description_tag.text.strip() if description_tag else "N/A"

        price_tag = soup.find("div", class_="plan_detail__azoZ2")
        details['Price Details'] = price_tag.text.strip() if price_tag else "N/A"

        contact_tag = soup.find("a", href=True, style="color: #C9FFFF")
        details['Contact Info'] = contact_tag['href'] if contact_tag else "N/A"
    except AttributeError as e:
        print(f"Error scraping {url}: {str(e)}")
        return None

    return details

def process_url(url):
    """
    Wrapper function to process a single URL with error handling.
    
    Args:
        url (str): URL to process
        
    Returns:
        dict: Scraped plan details or None if processing fails
    """
    try:
        print(f"Scraping: {url}")
        return scrape_plan_details(url)
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return None

def save_results(all_details):
    """
    Save scraped data in multiple formats (CSV, JSON, TXT).
    
    Args:
        all_details (list): List of dictionaries containing plan details
    """
    # Save to CSV
    with open("broadband_plans.csv", mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Title", "Description", "Price Details", "Contact Info"])
        for details in all_details:
            writer.writerow([
                details.get("Title", "N/A"),
                details.get("Description", "N/A"),
                details.get("Price Details", "N/A"),
                details.get("Contact Info", "N/A"),
            ])

    # Save to JSON
    with open("broadband_plans.json", mode="w", encoding="utf-8") as json_file:
        json.dump(all_details, json_file, indent=4, ensure_ascii=False)

    # Save to TXT
    with open("broadband_plans.txt", mode="w", encoding="utf-8") as txt_file:
        for idx, details in enumerate(all_details, start=1):
            txt_file.write(f"Plan {idx}:\n")
            for key, value in details.items():
                txt_file.write(f"{key}: {value}\n")
            txt_file.write("\n")

def main():
    """
    Main execution function that coordinates the scraping process.
    """
    # Get the main page content
    soup = get_page_content(MAIN_URL)
    if not soup:
        print("Error: Failed to fetch main page content")
        return

    # Extract all plan URLs
    plan_urls = scrape_links(soup)
    print(f"Found {len(plan_urls)} plans to process.")

    # Use multithreading to scrape plan details
    all_details = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = executor.map(process_url, plan_urls)
        all_details = [result for result in results if result]

    print(f"Successfully scraped {len(all_details)} plans.")
    
    # Save results in multiple formats
    save_results(all_details)
    print("Data has been saved to broadband_plans.csv, .json, and .txt")

if __name__ == "__main__":
    main()
