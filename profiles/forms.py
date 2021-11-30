from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-5 profile-form-input'
            self.fields[field].label = False

class ContactForm(forms.Form):
    """
    A general contact form
    """
    def __init__(self, *args, **kwargs):
        """
        Set placeholders
        """
        super().__init__(*args, **kwargs)
        self.fields['from_email'].widget.attrs['placeholder'] = 'Email'
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'

    from_email = forms.EmailField(required=True, max_length=254, label='Email')
    subject = forms.CharField(required=True, max_length=100)
    message = forms.CharField(required=True, widget=forms.Textarea)


    
