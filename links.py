import requests

def check_links(soup):
    broken = []
    for a in soup.find_all("a", href=True):
        link = a["href"]
        if link.startswith("http"):
            try:
                r = requests.head(link, timeout=5)
                if r.status_code >= 400:
                    broken.append(link)
            except:
                broken.append(link)
    return broken
