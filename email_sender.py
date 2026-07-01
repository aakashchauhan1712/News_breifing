import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_news_email(recipient_email: str, email_content: str):
    """
    Sends the generated news briefing text to a specified recipient.
    """
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))

    # 1. Construct the email structure
    msg = EmailMessage()
    msg["Subject"] = "Your Daily AI News Briefing 📰"
    msg["From"] = sender_email
    msg["To"] = recipient_email
    
    # Set content (Gemini returns Markdown text by default)
    msg.set_content(email_content)

    try:
        # 2. Open an encrypted connection to the SMTP server
        print(f"Connecting to server: {smtp_server}...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrades the connection to secure TLS encryption
            
            print("Logging into email account...")
            server.login(sender_email, sender_password)
            
            print(f"Sending email to {recipient_email}...")
            server.send_message(msg)
            
        print("✅ Email sent successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send email. Error: {e}")
        return False