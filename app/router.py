from fastapi import APIRouter
from app.email_reader import fetch_emails_imap
from app.email_model import Email

router = APIRouter()

@router.get("/emails", response_model=list[Email])
async def get_emails():
    emails = fetch_emails_imap()
    return emails
