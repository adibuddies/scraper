import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from urllib.request import urlretrieve

# Set up WebDriver (update path to your chromedriver)
CHROMEDRIVER_PATH = "path here"      #Add your path here

def setup_driver():
    options = webdriver.ChromeOptions()
    # Comment out the following line if you want to see the browser
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
    return driver

def scrape_images(query, max_images=500):
    query = query.replace(" ", "+")
    url = f"https://www.google.com/search?hl=en&tbm=isch&q={query}"
    
    driver = setup_driver()
    driver.get(url)
    time.sleep(random.randint(3, 11))  # Initial delay for the page to load
    
    # Create a folder to save images
    folder_path = "aircraft_images"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    downloaded = 0
    image_urls = set()  # Track already downloaded URLs
    retries = 0  # Keep track of retry attempts
    
    while downloaded < max_images:
        # Scroll to load more images
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(random.randint(3, 11))  # Random delay between scrolls
        
        # Find image elements
        image_elements = driver.find_elements(By.CSS_SELECTOR, "img")
        
        for img in image_elements:
            if downloaded >= max_images:
                break
            src = img.get_attribute("src")
            if src and src.startswith("http") and src not in image_urls:
                try:
                    # Save the image
                    img_name = os.path.join(folder_path, f"image_{downloaded + 1}.jpg")
                    urlretrieve(src, img_name)
                    image_urls.add(src)
                    print(f"Downloaded: {img_name}")
                    downloaded += 1
                except Exception as e:
                    print(f"Error downloading {src}: {e}")
        
        # Handle "Show more images" button
        try:
            show_more_button = driver.find_element(By.CSS_SELECTOR, ".mye4qd")
            show_more_button.click()
            time.sleep(random.randint(3, 11))  # Random delay after clicking
        except Exception:
            print("No 'Show more images' button found.")
            retries += 1
        
        # Wait for more images to load (up to 15 seconds)
        time.sleep(15)
        new_image_count = len(driver.find_elements(By.CSS_SELECTOR, "img"))
        if new_image_count <= len(image_urls) and retries > 3:
            print("No more new images to load. Ending scraping.")
            break

    driver.quit()
    print(f"Downloaded {downloaded} images.")

# Run the scraper
scrape_images("your query here", max_images=500)     #edit here
