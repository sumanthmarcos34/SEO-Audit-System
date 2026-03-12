def performance_metrics(html, soup):
    page_size_kb = len(html.encode("utf-8")) / 1024

    scripts = soup.find_all("script")
    blocking_scripts = [
        s.get("src") for s in scripts
        if s.get("src") and not s.has_attr("async") and not s.has_attr("defer")
    ]

    images = soup.find_all("img")
    missing_alt = len([img for img in images if not img.get("alt")])

    return {
        "page_size_kb": round(page_size_kb, 2),
        "total_scripts": len(scripts),
        "blocking_scripts": len(blocking_scripts),
        "images": len(images),
        "missing_alt": missing_alt
    }
