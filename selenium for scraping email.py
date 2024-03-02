from selenium import webdriver
from bs4 import BeautifulSoup
import re

# URLs of the webpages
urls = [
    "https://www.orbiosolutions.com/contact-us",
    # Add other URLs here if needed
]

emails = set()

# Iterate through each URL
for url in urls:
    driver = webdriver.Chrome()
    driver.get(url)

    # Parse the page source using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find email addresses in href attributes with "mailto:" prefix
    for tag in soup.find_all(href=re.compile("^mailto:")):
        email = tag['href'].split(":")[1]  # Extract email address
        emails.add(email)

    # Find email addresses in spans containing email addresses
    for span in soup.find_all('span', text=re.compile(r'[\w\.-]+@[\w\.-]+')):
        emails.add(span.text)
        
    # Find email addresses in h2 tags with class "media-email-icon"
    for h2 in soup.find_all('h2', class_='media-email-icon'):
        emails.add(h2.text.strip())

    driver.quit()

# Print found email addresses
for email in emails:
    print("Email address found:", email)
