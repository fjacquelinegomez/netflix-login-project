# Resources: https://github.com/mailersend/mailersend-python?tab=readme-ov-file#authentication


from mailersend.emails import NewEmail
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize MailerSend API
mailer = NewEmail(os.getenv('MAILERSEND_API_KEY'))

# Email setup
mail_body = {}

mail_from = {
    "name": "Netflix Support",
    "email": "pswdhelp4myflixsetup@gmail.com",
}

recipients = [
    {
        "name": "Fernanda",
        "email": "hbjackie02@gmail.com",
    }
]

variables = [
    {
        "email": "hbjackie02@gmail.com",
        "substitutions": [
            {
                "var": "foo",
                "value": "bar"
            },
        ]
    }
]

# Build email
mailer.set_mail_from(mail_from, mail_body)
mailer.set_mail_to(recipients, mail_body)
mailer.set_subject("Unusual Login Activity Detected on Your Netflix Account", mail_body)
mailer.set_template("3vz9dleqy11lkj50", mail_body)  # Replace with your actual template ID
mailer.set_personalization(variables, mail_body)

# Send email with error handling
try:
    response = mailer.send(mail_body)
    print("Email sent successfully:", response)
except Exception as e:
    print("Error sending email:", e)
