# Automated News Digest

This Python automation project scrapes top headlines from BBC and CNN, classifies them using an NLP model (zero-shot learning via HuggingFace Transformers), formats them into a categorized HTML digest, and sends the news via email.

> A seamless integration of web scraping, natural language processing, and email automation.

---

## Project Files

| File Name            | Description                                                             |
|----------------------|-------------------------------------------------------------------------|
| `news_emailer.py`    | Main script: scrapes, classifies, formats, and sends the email          |
| `scraper.py`         | Scrapes headlines from BBC and CNN using BeautifulSoup                  |
| `classifier.py`      | Classifies headlines using BART-based zero-shot classification           |
| `emailer.py`         | Formats headlines and sends emails via SMTP                             |
| `.env.example`       | Sample configuration file for environment variables                     |
| `Pipfile`            | Declares dependencies and virtual environment setup (via pipenv)        |
| `Pipfile.lock`       | Ensures reproducibility by locking dependency versions                  |

---

## Features

- Scrapes top news from **BBC** and **CNN**
- Classifies each headline into categories like Tech, Business, Politics, etc.
- Formats news into a readable, styled HTML email
- Sends email automatically to the configured recipient

---

## Technologies Used

- `requests`, `beautifulsoup4` – Web scraping
- `transformers` (BART) – Zero-shot classification
- `smtplib`, `email.mime` – Email delivery
- `dotenv` – Secure configuration handling
- `pipenv` – Dependency management and environment setup

---

