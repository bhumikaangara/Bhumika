import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Website URL
url = "https://quotes.toscrape.com"

# Step 2: Request website
response = requests.get(url)

# Step 3: Get HTML
html_content = response.text

# Step 4: Parse HTML
soup = BeautifulSoup(html_content, "html.parser")

# Step 5: Find all quotes
quotes = soup.find_all("div", class_="quote")

# Step 6: Store data
data = []

for quote in quotes:
    text = quote.find("span", class_="text")
    author = quote.find("small", class_="author")

    quote_text = text.text if text else "N/A"
    author_name = author.text if author else "N/A"

    data.append([quote_text, author_name])

# Step 7: Save to CSV
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    writer.writerows(data)

print("Task 13 Completed Successfully!")
