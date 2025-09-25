import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import List
from fastapi import HTTPException

# config.py
settings = {
    "EMAIL_HOST": "smtp.gmail.com",
    "EMAIL_PORT": 587
}

host = settings["EMAIL_HOST"]
port = settings["EMAIL_PORT"]

def send_email(
    subject: str,
    body: str,
    to_emails: List[str],
    from_email: str,
    password: str,
    attachments: List[str] = None,
    html: bool = False
):
    try:
        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = ", ".join(to_emails)
        msg["Subject"] = subject

        # Attach plain text or HTML
        if html:
            msg.attach(MIMEText(body, "html"))
        else:
            msg.attach(MIMEText(body, "plain"))

        # Attach files if any
        if attachments:
            for file_path in attachments:
                try:
                    with open(file_path, "rb") as attachment:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={file_path.split('/')[-1]}"
                    )
                    msg.attach(part)
                except Exception as e:
                    print(f"Could not attach file {file_path}: {e}")

        # Send securely
        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to send email. Please try again later."
        )
