from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

FROM_EMAIL = os.getenv("EMAIL_FROM")
TO_EMAIL = os.getenv("EMAIL_TO")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
LOGIN = os.getenv("EMAIL_LOGIN")
PASSWORD = os.getenv("EMAIL_PASSWORD")

def format_email(categorized_headlines):
    html = "<h1>🗞 Daily News Digest</h1>"
    for source, categories in categorized_headlines.items():
        html += f"<h2>{source}</h2>"
        for category, headlines in categories.items():
            html += f"<h3>{category}</h3><ul>"
            html += ''.join(f"<li>{headline}</li>" for headline in headlines)
            html += "</ul>"
        html += "<hr>"
    return html

def send_email(html_content):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Daily News Headlines"
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(LOGIN, PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
