from collections import Counter
import re
import requests
from urllib.parse import urljoin

def seo_analysis(soup, html, base_url):
    title = soup.title.string if soup.title else "Missing"
    meta_desc = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta_desc["content"] if meta_desc else "Missing"

    headings = {f"h{i}": len(soup.find_all(f"h{i}")) for i in range(1,7)}

    text = re.findall(r'\b[a-z]{4,}\b', soup.get_text().lower())
    keywords = Counter(text).most_common(10)

    robots = requests.get(urljoin(base_url, "/robots.txt")).status_code == 200
    sitemap = requests.get(urljoin(base_url, "/sitemap.xml")).status_code == 200

    return {
        "title": title,
        "meta_description": meta_desc,
        "headings": headings,
        "top_keywords": keywords,
        "robots_txt": robots,
        "sitemap": sitemap
    }
