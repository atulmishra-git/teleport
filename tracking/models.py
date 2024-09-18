import uuid
from django.db import models
from django.utils.timezone import now
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from customers.models import Customer


def validate_country(value):
    if not value.isalpha():
        raise ValidationError(
            "%(value)s is not string",
            params={"value": value},
        )


class Tracker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    weight = models.DecimalField(max_digits=10, decimal_places=3, default=0.000)
    created_at = models.DateTimeField(auto_now_add=now)
    origin_country_id = models.CharField(max_length=2, blank=False, validators=[validate_country])
    destination_country_id = models.CharField(max_length=2, blank=False, validators=[validate_country])
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="tracker_customer")
    tracking_number = models.CharField(max_length=16, blank=False, unique=True, validators=[
        RegexValidator("^[A-Z0-9]{1,16}$")
    ])

    class Meta:
        ordering = ['-id']
    
    def __str__(self) -> str:
        return self.id
    


