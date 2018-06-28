from django import forms
from .models import signup,marksheet,twitter,currency,rss,chat
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
class marksheetform(forms.ModelForm):
    class Meta:
        model = marksheet
        fields = ["fullname","mark"]

class twitterform(forms.ModelForm):
    class Meta:
        model = twitter
        fields = ["fullname"]
class currencyform(forms.ModelForm):
    class Meta:
        model = currency
        fields = ["fro","to","amount"]
class rssform(forms.ModelForm):
    class Meta:
        model = rss
        fields = ["url"]
class chatform(forms.ModelForm):
    class Meta:
        model = chat
        fields = ["msg"]
