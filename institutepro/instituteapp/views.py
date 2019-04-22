from django.shortcuts import render
from .models import ContactData, FeedbackData
from forms import ContactForm, FeedbackForm
from django.http.response import HttpResponse


def home(request):
    return render(request,'institute_home.html')


def ContactView(request):
    if request.method=='POST':
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name=cform.cleaned_data.get('name','')
            email=cform.cleaned_data.get('email','')
            mobile=cform.cleaned_data.get('mobile','')
            courses=cform.cleaned_data.get('courses','')
            locations=cform.cleaned_data.get('locations','')
            shift=cform.cleaned_data.get('shift','')

            data=ContactData(
                name=name,
                email=email,
                mobile=mobile,
                courses=courses,
                locations=locations,
                shift=shift
            )
            data.save()
            cform = ContactForm()
            return render(request, 'institute_contact.html', {'cform': cform})
        #else:
            #return HttpResponse("enter all fields")

    else:
        cform=ContactForm()
        return render(request,'institute_contact.html',{'cform':cform})

def services(request):
    return render(request,'institute_service.html')


import datetime as dt
date1=dt.datetime.now()
def FeedbackView(request):
    if request.method=='POST':
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name','')
            rating=request.POST.get('rating','')
            feedback=request.POST.get('feedback','')

            data=FeedbackData(
                name=name,
                rating=rating,
                date=date1,
                feedback=feedback
            )
            data.save()
            fform=FeedbackForm()
            feedbacks=FeedbackData.objects.all()
            return render(request,'institute_feedback.html',{'fform':fform,'feedbacks':feedbacks})
        else:
            return HttpResponse("Enter all fields")

    else:
        fform=FeedbackForm()
        feedbacks = FeedbackData.objects.all()
        return render(request,'institute_feedback.html',{'fform':fform,'feedbacks':feedbacks})


def GalleryView(request):
    return render(request,'institute_gallery.html')