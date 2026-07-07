import smtplib
from email.message import EmailMessage
from config import EMAIL, APP_PASSWORD

receiver = input("Enter receiver email: ")
subject = input("Enter subject: ")
message = input("Enter message: ")
file_path = input("Enter file path: ")

msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = receiver
msg["Subject"] = subject
msg.set_content(message)

with open(file_path, "rb") as f:
    file_data = f.read()
    file_name = file_path.split("\\")[-1]
    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="octet-stream",
        filename=file_name,
    )

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL, APP_PASSWORD)
    smtp.send_message(msg)

print("✅ Email with attachment sent successfully!")