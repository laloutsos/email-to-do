from imapclient import IMAPClient

HOST = 'imap.gmail.com'
USERNAME = 'your.email@gmail.com'
PASSWORD = 'your_app_password'

with IMAPClient(HOST, ssl=True) as server:
    try:
        server.login(USERNAME, PASSWORD)
        print("Login successful!")
    except Exception as e:
        print(f"Login failed: {e}")
