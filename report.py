from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(report_path, seo, perf, links, summary):
    c = canvas.Canvas(report_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, height - 40, "Website SEO & Performance Audit")

    c.setFont("Helvetica", 11)
    y = height - 80

    for k, v in seo.items():
        c.drawString(40, y, f"{k}: {v}")
        y -= 15

    y -= 20
    c.drawString(40, y, f"Performance Metrics: {perf}")
    y -= 20
    c.drawString(40, y, f"Broken Links: {len(links)}")

    c.showPage()

    c.setFont("Helvetica", 11)
    text = c.beginText(40, height - 50)
    text.textLines(summary)
    c.drawText(text)

    c.save()
