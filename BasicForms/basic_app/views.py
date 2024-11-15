from django.shortcuts import render, redirect
from basic_app import forms
from basic_app.models import UserData

# Initial homepage
def index(request):
    return render(request, "index.html")

# Form page
def form_name_view(request):
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            data = form.cleaned_data  # Access cleaned_data only after validation
            user_data = UserData(
                name = data["name"],
                email = data["email"],
                text = data["text"]
            )

            user_data.save()
            print("Validation sucess!!!")
            return render(request, "success.html")
            
        else:
            print(form.errors)  # Debug any validation errors
    else:
        # Initialize an empty form for GET request
        form = forms.FormName()
    
    # Render the form page with the form instance
    return render(request, "form_page.html", {"form": form})

# After successful submission show success.html
def form_success(request):
    return render(request, "success.html")
