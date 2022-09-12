from django import forms
class emailsendform(forms.Form):
    toemail=forms.CharField()
    subject=forms.CharField()
    fromemail=forms.CharField()
    body=forms.CharField()



