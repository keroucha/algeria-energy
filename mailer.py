"""إرسال إشعار للمالك عند دخول زائر جديد (في خيط خلفي كي لا يتأخر الموقع)."""
import logging
import os
import smtplib
import threading
from datetime import datetime
from email.message import EmailMessage

log = logging.getLogger("mailer")


def _send(visitor_email: str, lang: str, ip: str) -> None:
    host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    port = int(os.getenv("SMTP_PORT", "587"))
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")
    owner = os.getenv("OWNER_EMAIL") or user
    if not (user and password and owner):
        log.warning("SMTP غير مضبوط؛ لم يُرسل الإشعار. الزائر: %s (%s)", visitor_email, lang)
        return
    msg = EmailMessage()
    msg["Subject"] = "زائر جديد دخل الموقع"
    msg["From"] = user
    msg["To"] = owner
    msg["Reply-To"] = visitor_email
    msg.set_content(
        "دخل شخص جديد إلى الموقع:\n\n"
        f"البريد الإلكتروني: {visitor_email}\n"
        f"اللغة: {lang}\n"
        f"الوقت: {datetime.now():%Y-%m-%d %H:%M:%S}\n"
        f"IP: {ip}\n"
    )
    try:
        with smtplib.SMTP(host, port, timeout=15) as s:
            s.starttls()
            s.login(user, password)
            s.send_message(msg)
    except Exception:
        log.exception("فشل إرسال الإشعار")


def notify_owner(visitor_email: str, lang: str, ip: str) -> None:
    threading.Thread(target=_send, args=(visitor_email, lang, ip), daemon=True).start()
