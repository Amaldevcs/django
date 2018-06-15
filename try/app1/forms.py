from django import forms
from .models import signup
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




