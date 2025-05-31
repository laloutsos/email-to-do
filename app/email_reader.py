from imapclient import IMAPClient
import pyzmail
from datetime import datetime
import html2text
import re
#import getpass

from app.email_model import Email
import time

HOST = 'imap.gmail.com'

def clean_body(body: str) -> str:
    stop_phrases = [
        "See more people you might know",
        "Unsubscribe:",
        "This email was intended for",
        "© 2025 LinkedIn Corporation",
        "Learn why we included this",
        "Read more:",
        "LIKE PRAISE EMPATHY",
        "See more on LinkedIn:",
        "https://",
    ]

    for phrase in stop_phrases:
        index = body.find(phrase)
        if index != -1:
            body = body[:index].strip()

    body = re.sub(r'http\S+', '', body)
    body = re.sub(r'\b[\d,]{3,}\b', '', body)
    body = re.sub(r'\[.*?\]', '', body)
    body = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', body)
    body = re.sub(r'\n{2,}', '\n\n', body)
    body = re.sub(r'[ \t]{2,}', ' ', body)

    return body.strip()


def fetch_emails_imap(USERNAME,PASSWORD):
    emails = []

    with IMAPClient(HOST) as server:
        server.login(USERNAME, PASSWORD)
        server.select_folder('INBOX', readonly=True)

        messages = server.search(['ALL'])
        messages = messages[-1:]

        for msgid, data in server.fetch(messages, ['ENVELOPE', 'BODY[]']).items():
            message = pyzmail.PyzMessage.factory(data[b'BODY[]'])

            subject = message.get_subject()
            from_email = message.get_addresses('from')[0][1] if message.get_addresses('from') else None
            to_email = message.get_addresses('to')[0][1] if message.get_addresses('to') else None

            if message.text_part:
                body = message.text_part.get_payload().decode(message.text_part.charset)
            elif message.html_part:
                html = message.html_part.get_payload().decode(message.html_part.charset)
                body = html2text.html2text(html)
            else:
                body = ""

            body = clean_body(body)

            date_header = message.get_decoded_header('date')
            try:
                date_obj = datetime.strptime(date_header[:-6], '%a, %d %b %Y %H:%M:%S')
            except Exception:
                date_obj = datetime.now()


            email_obj = Email(
                subject=subject,
                body=body,
                from_email=from_email,
                to_email=to_email,
                date=date_obj,
                message_id=str(msgid),
                #summary=summary
            )
            emails.append(email_obj)
    return emails


if __name__ == "__main__":
    USERNAME = input("Type your email: ")
    PASSWORD = input("Type your password: ")
    print("Connecting...")
    try:
        while True:
            emails = fetch_emails_imap(USERNAME, PASSWORD)
            for e in emails:
                print(f"Subject: {e.subject}")
                print(f"From: {e.from_email}")
                print(f"Date: {e.date}")
                print("Body:")
                print(e.body)
                print("Summary:")
                print(e.summary)
                print("-" * 40)

            print("Waiting 5 minutes before next fetch...")
            time.sleep(300)

    except KeyboardInterrupt:
        print("\nStopped by user. Exiting gracefully...")

