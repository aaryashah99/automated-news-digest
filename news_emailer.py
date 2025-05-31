import scraper
from classifier import classify_headline
from emailer import format_email, send_email

# Scrape headlines
bbc_headlines = scraper.scrape_bbc()
cnn_headlines = scraper.scrape_cnn()


def categorize(source, headlines):
    cat_map = {}
    for headline in headlines:
        category = classify_headline(headline)
        cat_map.setdefault(category, []).append(headline)
    return cat_map


# Categorize headlines
all_headlines = {
    "BBC": categorize("BBC", bbc_headlines),
    "CNN": categorize("CNN", cnn_headlines),
}

# Format and send email
html = format_email(all_headlines)
send_email(html)

print("News email sent successfully.")
