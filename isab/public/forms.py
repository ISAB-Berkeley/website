from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=3,
        max_length=30,
        label="",
        help_text="",
        error_messages={'min_length': 'Your name is too short.'},
        widget=forms.TextInput(
            attrs={'placeholder': 'Name*'}
        )
    )
    email = forms.EmailField(
        max_length=255,
        label="",
        help_text="",
        widget=forms.TextInput(
            attrs={'placeholder': 'E-mail*'}
        )
    )
    subject = forms.CharField(
        max_length=300,
        label="",
        help_text="",
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Subject'}
        )
    )
    comment = forms.CharField(
        max_length=2000,
        label="",
        help_text="",
        widget=forms.Textarea(
            attrs={'placeholder': 'Message*'}
        )
    )