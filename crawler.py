import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def crawl(start_url, max_pages=10):
    """Crawl pages starting from start_url, staying on the same domain."""
    visited = set()
    to_visit = [start_url]
    results = []
    domain = urlparse(start_url).netloc

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)

        if url in visited:
            continue

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Skipping {url}: {e}")
            visited.add(url)
            continue

        # Only process HTML pages
        if "text/html" not in response.headers.get("Content-Type", ""):
            visited.add(url)
            continue

        visited.add(url)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title and soup.title.string else "No title"
        results.append({"url": url, "title": title})
        print(f"Crawled: {url} -> {title}")

        # Find all links on the page
        for link in soup.find_all("a", href=True):
            full_url = urljoin(url, link["href"])
            full_url = full_url.split("#")[0]  # remove fragments

            # Stay on the same domain and skip already-seen links
            if urlparse(full_url).netloc == domain and full_url not in visited:
                to_visit.append(full_url)

    return results


if __name__ == "__main__":
    pages = crawl("https://books.toscrape.com", max_pages=10)
    print(f"\nDone! Crawled {len(pages)} pages.")