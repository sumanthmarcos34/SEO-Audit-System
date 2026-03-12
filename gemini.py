def generate_summary(audit_data: dict) -> str:
    """
    Fallback summary.
    Gemini integration temporarily disabled to avoid SDK issues.
    """

    return (
        "Executive Summary:\n"
        "The website was analyzed for SEO and performance fundamentals. "
        "Key areas such as metadata, headings, page size, and assets were reviewed.\n\n"
        "SEO Recommendations:\n"
        "- Ensure proper title and meta description usage\n"
        "- Improve heading hierarchy\n"
        "- Fix broken links and missing alt attributes\n\n"
        "Performance Recommendations:\n"
        "- Reduce page size\n"
        "- Minimize blocking scripts\n"
        "- Optimize images\n"
    )
