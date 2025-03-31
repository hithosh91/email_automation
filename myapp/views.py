from .models import contact
from django.core.mail import send_mail
from django.http import HttpResponse  # Corrected from httpResponse to HttpResponse
from django.conf import settings  # Corrected from django.config to django.conf


# Create your views here.
def send_automated_email(request):
    # Correct model name and query method
    contacts = contact.objects.all()  # Changed object() to objects

    subject = "Welcome to Django automated email system!"

    for emaild in contacts:
        message = f"Hello {emaild.name}, welcome to my Django email world."

        # Send email to each contact
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,  # Updated from DEFAULT_FROM_EMAIL
            recipient_list=[emaild.email],
            fail_silently=False,
        )

    return HttpResponse("✅ Successfully sent all emails!")
