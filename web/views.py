import json

from multiprocessing import context
from turtle import title
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from web.models import FAQ_TYPE, Promoter, Testimonial, Faq, Subscribe


# Create your views here.
def index(request):
    testimonials = Testimonial.objects.all()
    promoters = Promoter.objects.all()
    rent_tracking_faqs = Faq.objects.filter(faq_type="rent tracking")
    new_deposit_faqs = Faq.objects.filter(faq_type="new_deposit")
    existing_deposit_faqs = Faq.objects.filter(faq_type="existing_deposit")
    context = {
        "testimonials": testimonials,
        "promoters": promoters,
        "rent_tracking_faqs": rent_tracking_faqs,
        "new_deposit_faqs": new_deposit_faqs,
        "existing_deposit_faqs":  existing_deposit_faqs


    }
    return render(request, "index.html", context=context)


def subscribe(request):
    email = request.POST.get('email')

    if not Subscribe.objects.filter(email=email).exists():
        Subscribe.objects.create(
            email=email,

        )
        response_data = {
            "status": "success",
            "title": "Successfully Registered",
            "message": "Subscribe successfully"
        }
    else:
        response_data = {
            "status": "error",
            "title": "Your are already registered",
            "message": "You are already a member. No need to register"
        }

    return HttpResponse(json.dumps(response_data), content_type="application/javascript")
