# Python Mail Sender

A simple Python project to send emails using Gmail SMTP.

## Features
- Send emails using Gmail
- Send custom subject and message
- Send file attachments
- Uses environment variables (.env) to keep credentials secure

## Technologies Used
- Python
- smtplib
- python-dotenv
- email.message

## How to Run
1. Install requirements:
   pip install -r requirements.txt

2. Create a .env file:
   EMAIL=your_email@gmail.com
   APP_PASSWORD=your_app_password

3. Run:
   python main.py
