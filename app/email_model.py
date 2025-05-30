from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class Email(BaseModel):
    subject: str
    body: str
    from_email: EmailStr
    to_email: Optional[EmailStr]
    date: datetime
    message_id: Optional[str]
    summary: Optional[str] = None