from django import forms
from multiselectfield import MultiSelectFormField

class ContactForm(forms.Form):
    name=forms.CharField(
        label="Enter Your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your name'
            }
        )
    )

    email=forms.EmailField(
        label="Enter Your email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your email'
            }
        )
    )

    mobile=forms.IntegerField(
        label="Enter Your mobile",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your mobile'
            }
        )
    )

    COURSE_CHOICES = (
        ('python', 'Python'),
        ('django', 'Django'),
        ('restapi', 'RestAPI'),
        ('ui', 'UI')

    )
    courses = MultiSelectFormField(max_length=50, choices=COURSE_CHOICES)

    LOCATION_CHOICES=(
        ('hyd','Hyderabad'),
        ('bang','Bangalore'),
        ('che','Chennai')
    )
    locations=MultiSelectFormField(max_length=50,choices=LOCATION_CHOICES)
    SHIFT_CHOICES = (
        ('mrng', 'Morning'),
        ('aftn', 'Afternoon'),
        ('eve', 'Evening'),
        ('nite', 'Night')

    )
    shift = MultiSelectFormField(max_length=50, choices=SHIFT_CHOICES)



class FeedbackForm(forms.Form):

    name=forms.CharField(
        label="Enter Your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your name'
            }
        )
    )
    rating=forms.IntegerField(
        label="Enter Your rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your rating'
            }
        )
    )

    feedback=forms.CharField(
        label="Enter Your name",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your feedback'
            }
        )
    )

