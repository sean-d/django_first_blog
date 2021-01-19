from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email_address = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
