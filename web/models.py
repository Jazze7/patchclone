from django.db import models


FAQ_TYPE = (
    ("rent tracking", "Rent Tracking"),
    ("new_deposit", "New Deposit"),
    ("existing_deposit", "Existing Deposit"),
)
# Create your models here.


class Testimonial(models.Model):
    name = models.CharField(max_length=255, default='Jazzi')
    designation = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="testimonials/")

    def __str__(self):
        return self.name


class Promoter(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="promoters/")

    def __str__(self):
        return self.name


class Faq(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    faq_type = models.CharField(max_length=255, choices=FAQ_TYPE)

    def __str__(self):
        return self.title


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
