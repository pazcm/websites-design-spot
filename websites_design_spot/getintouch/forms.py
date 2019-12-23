from django import forms

class GetInTouchForm(forms.Form):
    contact_name = forms.CharField(required=True, label="First Name")
    contact_surname= forms.CharField(required=False, label="Last Name")
    from_email = forms.EmailField(required=True, label="Email")
    contact_website = forms.CharField(required=False, label="Website")
    contact_company = forms.CharField(required=False, label="Company")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Message")