# Email Fetcher & Reader API

A Python project to fetch, clean, and serve emails via a REST API built with FastAPI.

---

## Project Overview

This project consists of several modules working together to retrieve emails from an IMAP server, process them, and expose them through a FastAPI endpoint.

---

## File Descriptions

### 1. `email_reader.py`

- **Purpose:** Connects to the IMAP server (e.g., Gmail) using `IMAPClient` and fetches emails from the inbox.
- **Functionality:**
  - Logs into the IMAP server with given credentials.
  - Fetches recent emails (last one or last 20 emails).
  - Extracts email metadata: subject, sender, recipient, date, message ID.
  - Retrieves the email body (supports plain text and HTML).
  - Cleans the email body by removing unwanted phrases, links, and formatting artifacts.
- **Key function:** `fetch_emails_imap(USERNAME, PASSWORD)` which returns a list of `Email` objects.

---

### 2. `email_model.py`

- **Purpose:** Defines the Pydantic data model representing an email.
- **Fields:**
  - `subject`: Email subject line (string).
  - `body`: Cleaned content of the email (string).
  - `from_email`: Sender's email address (validated email string).
  - `to_email`: Recipient's email address (optional).
  - `date`: Date and time the email was sent (datetime).
  - `message_id`: Optional unique ID of the email message.
- **Use:** Ensures consistent data validation and serialization when serving emails via API.

---

### 3. `router.py`

- **Purpose:** Defines the FastAPI router that handles API requests.
- **Functionality:**
  - Contains the `/emails` endpoint.
  - When called, it invokes `fetch_emails_imap` to retrieve emails and returns them as JSON using the `Email` model.
- **Usage:** Imported and included in the main FastAPI app for modular routing.

---

### 4. `main.py` (FastAPI app entrypoint)

- **Purpose:** Initializes the FastAPI application.
- **Functionality:**
  - Creates the FastAPI app instance with a custom title.
  - Includes the router with the `/emails` endpoint.
  - Serves as the entrypoint for running the API server.

---

## How It Works Together

- The user runs the FastAPI app (`main.py`), which serves the `/emails` API.
- When `/emails` is requested, `router.py` calls `fetch_emails_imap` from `email_reader.py`.
- `email_reader.py` logs into the IMAP server, fetches and cleans emails, and returns a list of `Email` Pydantic models defined in `email_model.py`.
- The API responds with the structured JSON list of emails.
---

## Getting Started

1. Set up your Python environment and install dependencies.
2. Configure your Gmail or IMAP credentials securely.
3. Run the FastAPI app:

```bash
uvicorn app.main:app --reload
```
---
Sure! Here's a polished, clear, and professional way to write that section in English for your README:

---

## Project Status

**🚧 This project is still under development. 🚧**

### Planned Future Improvements

* Save fetched emails to JSON files for persistent storage.
* Automatically generate concise summaries of email content.
* Organize emails based on the recipient.
* Maintain and manage duplicates to avoid repeated entries.

---

