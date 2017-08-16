from django import forms
from .validators import validate_url


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url])
    """
    def clean(self):
        cleaned_data = super(SubmitUrlForm, self).clean()
        print(cleaned_data)
        url = cleaned_data.get('url')

    def clean_url(self):
        url = self.cleaned_data['url']
        print(url)
        url_valudator = URLValidator()
        try:
            url_valudator(url)
        except:
            raise forms.ValidationError("Invalid URL")
        return url
    """