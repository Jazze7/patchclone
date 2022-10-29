from django.contrib import admin
from web.models import Faq, Promoter, Testimonial, Subscribe


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "image", "designation"]


# Register your models here.
admin.site.register(Testimonial, TestimonialAdmin)


class PromoterAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image"]


admin.site.register(Promoter, PromoterAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "faq_type", "description"]


admin.site.register(Faq, FaqAdmin)


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ["id", "email"]


admin.site.register(Subscribe, SubscribeAdmin)
