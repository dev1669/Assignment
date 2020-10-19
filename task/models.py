from django.db import models
import datetime

# Create your models here.

# Model for lead table
class Lead(models.Model):
    contact_person_name = models.CharField(max_length=255, default='abc', primary_key=True)
    phone_number = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    source = models.TextField(null=True)
    current_stage = models.TextField(null=True)
    last_follow_up_date = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name_plural = 'Lead'

    def __str__(self):
        return self.contact_person_name


# Model for Folow_up table

class Followup(models.Model):

    medium_choice = (
        ('Phone Call','Phone Call'),
        ('WhatsApp','WhatsApp'),
        ('Email','Email'),
    )

    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    follo_up_date = models.DateField(default=datetime.date.today)
    response = models.CharField(max_length=500)
    medium = models.CharField(max_length=100,choices=medium_choice)

    class Meta:
        verbose_name_plural = 'Follow Up'


class Lead_fields(models.Model):

    fields = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Lead Fields'


