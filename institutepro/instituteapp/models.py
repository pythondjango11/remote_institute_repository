from django.db import models
from multiselectfield import MultiSelectField

class ContactData(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.BigIntegerField()
    COURSE_CHOICES=(
        ('python','Python'),
        ('django','Django'),
        ('restapi','RestAPI'),
        ('ui','UI')

    )
    courses=MultiSelectField(max_length=50,choices=COURSE_CHOICES)
    LOCATION_CHOICES=(
        ('hyd','Hyderabad'),
        ('bang','Bangalore'),
        ('che','Chennai')
    )
    locations=MultiSelectField(max_length=50,choices=LOCATION_CHOICES)
    SHIFT_CHOICES=(
        ('mrng','Morning'),
        ('aftn', 'Afternoon'),
        ('eve','Evening'),
        ('nite','Night')

    )
    shift=MultiSelectField(max_length=50,choices=SHIFT_CHOICES)


class FeedbackData(models.Model):
    name=models.CharField(max_length=50)
    rating=models.IntegerField()
    date=models.DateField()
    feedback=models.TextField(max_length=500)

