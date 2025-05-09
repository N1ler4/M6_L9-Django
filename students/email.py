from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


def send_to_mail(subject , message , user_email):
    send_mail(
        subject=subject,
        message=message,
        from_email=EMAIL_HOST_USER,
        fail_silently=[user_email, ]
    )
    return True