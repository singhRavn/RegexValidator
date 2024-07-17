from django.db import models

from django.core.validators import RegexValidator

# Create your models here.

class Vehicle(models.Model):
    registration_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{3}\d{3}$',
                message="Enter a valid registration number in the format ABC123.",
                code="invalid_registration",
            ),
        ],
    )

    def __str__(self):
        return self.registration_number
