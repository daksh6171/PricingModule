from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from .models import (
    PricingConfig,
    DistanceBasePrice,
    DistanceAdditionalPrice,
    TimeMultiplierFactor,
    Users,
)


@shared_task
def my_task():
    pricing_config = PricingConfig.objects.filter(is_enabled=True)
    dbp = DistanceBasePrice.objects.filter(pricing_config=pricing_config)
    dap = DistanceAdditionalPrice.objects.filter(pricing_config=pricing_config)
    tmf = TimeMultiplierFactor.objects.filter(pricing_config=pricing_config)
    report = {"base price": dbp, "additional price": dap, "multiplier factor": tmf}
    print("Mail sending.......")
    subject = "sending report"
    message = report
    email_from = settings.EMAIL_HOST_USER
    email_list = Users.objects.all()
    recipient_list = list(email_list.values_list('email'))
    # recipient_list=['dakshbindal18@gmail.com',]
    print(recipient_list)
    send_mail(subject, message, email_from, recipient_list)
    return "mail has been sent....."
