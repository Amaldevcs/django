from django import forms
from .models import signup,company,apply,appliedd
class contactform(forms.Form):
    fullname = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

class signupform(forms.ModelForm):
    class Meta:
        model =signup
        fields =["email","fullname"]        
        def clean_email(self):



            email = self.cleaned_data.get('email')
            base,provider =email.split('@')
            domain,exten =provider.split('.')
            if not exten == 'com':

                raise forms.ValidationError("please enter valid email with .com extention")
            return email
class companyform(forms.ModelForm):
    class Meta:
        model = company
        
        fields = ["fullname","position","salary"]

class applyform(forms.ModelForm):
    class Meta:
        model = apply
        
        fields = ["fullname","email","userid"]
class appliedform(forms.ModelForm):
    class Meta:
        model = appliedd
        
        fields = ["email"]