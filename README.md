# Simple Web Crawler

A small web crawler built with Python that starts from a URL, follows links within the same domain, and lists the pages it finds along with their titles. It comes with a Flask web interface.

**Live demo:** https://simple-web-crawler-bbi12.onrender.com/

## Features
- Crawls pages starting from any URL
- Stays within the same domain
- Extracts page titles and links
- Limits the crawl to 10 pages by default
- Simple web form interface built with Flask

## Tech Stack
- Python
- Requests
- BeautifulSoup4
- Flask
- Gunicorn
- Deployed on Render

## Run Locally

```bash
git clone https://github.com/YOUR-USERNAME/simple-web-crawler.git
cd simple-web-crawler
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## How It Works
1. Starts at the URL you enter
2. Downloads the page and extracts its title
3. Collects all links on that page
4. Follows links on the same domain until the page limit is reached

## Note
Please only crawl websites you have permission to crawl. `books.toscrape.com` is a practice site made for this purpose.