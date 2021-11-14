from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class ContactId(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message='Wrong number format! '
                                         'Use format +380953618000')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    company = models.CharField(max_length=20)
    notes = models.TextField(max_length=255)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    def modified_contact(self):
        self.date_modified = timezone.now()
        self.save()
