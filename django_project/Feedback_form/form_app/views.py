from django.shortcuts import render,redirect
from form_app import forms
from .models import StoreFeedback

# Create your views here.

def index(request):
    return render (request,'index.html')


def feedback(request):
    form = forms.FeedbackForm() #object of class FeedbackForm is created

 #here we are creating the object and adding manually to the database because we have used forms.FeedbackForm
 #instead of that if we use forms.ModelForm in forms.py file then we don't need this.

    if request.method == "POST":
        form = forms.FeedbackForm(request.POST) #post request is sent and data is taken in form
        if form.is_valid():                      #if the input data is valid then create a object of StoreFeedback and add data to it 
                                                #so as to store it in database
            StoreFeedback.objects.create(
                
                name = form.cleaned_data['name'],  #here the name in bracket is from forms.py and left side name is from models.py
                email_id = form.cleaned_data['email'],
                comment=form.cleaned_data['feedback']
            )                                                 
            return redirect('success')
        else:
            print("Invalid Form!!")
            
    return render (request,'feedback.html',{'form':form})

def success(request):
    return render (request,'success.html')