from fastapi import FastAPI
from pydantic import BaseModel
from audit.crawler import fetch_page
from audit.seo import seo_analysis
from audit.performance import performance_metrics
from audit.links import check_links
from audit.gemini import generate_summary
from audit.report import generate_pdf
import os

app = FastAPI()

class AuditRequest(BaseModel):
    url: str

@app.post("/audit")
def audit_site(req: AuditRequest):
    soup, html = fetch_page(req.url)

    seo = seo_analysis(soup, html, req.url)
    perf = performance_metrics(html, soup)
    links = check_links(soup)

    audit_data = {
        "seo": seo,
        "performance": perf,
        "broken_links": links
    }

    summary = generate_summary(audit_data)

    filename = req.url.replace("https://", "").replace("/", "_")
    path = f"reports/{filename}_audit.pdf"
    generate_pdf(path, seo, perf, links, summary)

    return {"status": "success", "report_path": path}
