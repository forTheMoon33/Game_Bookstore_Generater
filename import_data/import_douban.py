import requests
from bs4 import BeautifulSoup
import pandas as pd

# Example: search for a keyword
keyword = "Python"
url = f"https://book.douban.com/subject_search?search_text={keyword}&cat=1001"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

books = []

# Parse book info (title, author, etc.)
for item in soup.select(".subject-item"):
    title_tag = item.select_one("h2 a")
    title = title_tag.get_text(strip=True) if title_tag else ""
    
    info_tag = item.select_one(".pub")
    info_text = info_tag.get_text(strip=True) if info_tag else ""
    
    # Split info (usually: author / publisher / year)
    info_parts = info_text.split("/")
    author = info_parts[0].strip() if len(info_parts) > 0 else ""
    publisher = info_parts[1].strip() if len(info_parts) > 1 else ""
    year = info_parts[2].strip() if len(info_parts) > 2 else ""
    
    books.append({
        "title": title,
        "author": author,
        "publisher": publisher,
        "year": year
    })

# Save to CSV
df = pd.DataFrame(books)
df.to_csv("douban_books.csv", index=False, encoding="utf-8-sig")

print(f"{len(books)} books saved to douban_books.csv")
