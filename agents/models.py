from django.db import models
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

from dental.choices import *

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    . fields.
    updating ``created`` and ``modified``
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Facility(TimeStampedModel):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(default="+41524204242")
    address = models.TextField(\
        default="123 Example Ln\nSpringfield, IL\n55555")
    public_email = models.EmailField(default="JaneDoe@example.com")
    accept_appointment_types = \
        MultiSelectField(choices=APPOINTMENT_TYPES, default=["Teeth Whitening"])
    accept_dental_plans = models.TextField(default="Aetna")
    accept_uninsured = models.NullBooleanField()
    accept_walkins = models.NullBooleanField()

    def __str__(self):
        return str(self.name)


class Agent(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    facility = models.OneToOneField(Facility)
