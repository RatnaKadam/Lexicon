from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    feedback = forms.CharField(max_length=200,widget=forms.Textarea)


#Instead of above, we can directly write, 
# because of this the instance of database will be directly crated and we don't need to create it manually
#class FeedbackForm(forms.ModelForm):
    #class Meta:
     #   model = Feedback
      #  fields = ['name', 'email', 'message']