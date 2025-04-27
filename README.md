# BookScraper 📚

**BookScraper** is a Python command-line tool that scrapes book titles and prices from [Books to Scrape](https://books.toscrape.com/). It allows you to fetch books from a specific category and save the results in a well-formatted text file or a structured JSON file.

---
## 🔧 Features

- Scrapes book titles and prices by category
- Uses `requests`, `BeautifulSoup`, `re`, and `tabulate` for web scraping and formatting
- Saves results in either `.txt` (pretty table) or `.json` format
- User-friendly and interactive command-line interface
- Supports UTF-8 encoding for file outputs

## 📦 Requirements

Make sure you have Python 3.6+ installed. Then, install the required libraries:

```bash
pip install requests beautifulsoup4 tabulate
```

## 🚀 Usage

Run the script in your terminal:

```bash
python book_scraper.py
```

You will be prompted to:

1. Enter the book category you want to scrape (e.g., `travel`, `humor`, `novels`, etc.).
2. Choose whether to save the results as a `.txt` file.
3. Choose whether to save the results as a `.json` file.

## 🧠 **Notes**

- If the category name has two words, use a dash - between them.
Example:
    - ✅ science-fiction
    - ✅ historical-fiction
- The category name must exist on [Books to Scrape](https://books.toscrape.com/).

- **Important:** You must set your own **User-Agent** inside the script before running it.  
  To do this, replace the `user-agent` field inside the `headers` dictionary with your real browser's User-Agent string.

Example:

```python
headers = {
    'user-agent': 'your actual User-Agent here'
}
```

> **Tip:** To find your User-Agent, you can visit [https://www.whatismybrowser.com/](https://www.whatismybrowser.com/) and copy the string.

- The script **will not work** without a valid User-Agent.

## 📁 Output Examples

### 📄 Text file (TXT):

```text
Type: travel
Date: 27/04/2025
================================================

╒════════════════════════════════╤════════════╕
│ Title                          │ Price      │
╞════════════════════════════════╪════════════╡
│ It's Only the Himalayas        │ £45.17     │
│ Full Moon over Noah's Ark      │ £49.43     │
│ See America: A Celebration...  │ £48.87     │
╘════════════════════════════════╧════════════╛
```

### 🗂️ JSON file:

```json
[
  { "Title": "It's Only the Himalayas", "Price": "£45.17" },
  { "Title": "Full Moon over Noah's Ark", "Price": "£49.43" },
  { "Title": "See America: A Celebration...", "Price": "£48.87" }
]
```

## 📄 **License**

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
