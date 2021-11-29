from django import forms
from .models import UserProfile, Suggestion


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

class SuggestionForm(forms.ModelForm):
    """
    A form for Reviews.
    """
    class Meta:
        # Set model
        model = Suggestion
        # Set field names
        fields = ('suggestion',)
        # Set field labels
        labels = {
            'suggestion': 'Suggestion',
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        """
        super().__init__(*args, **kwargs)
        # Set placeholders
        placeholders = {
            'suggestion': 'Suggestion',
        }
        # Set autofocus to review field
        self.fields['suggestion'].widget.attrs['autofocus'] = True
        # Loop through fields, add placeholders
        for field_name, placeholder in placeholders.items():
            # Add a * to placeholder if field is required
            if self.fields[field_name].required:
                placeholder_text = placeholder + "*"
            else:
                placeholder_text = placeholder
            # Set placeholder
            self.fields[field_name].widget.attrs[
                'placeholder'] = placeholder_text
            # Add review-input class
            self.fields[field_name].widget.attrs[
                'class'] = 'review-input'
