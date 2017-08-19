from django import forms
from .validators import validate_url


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='',
                          validators=[validate_url],
                          widget=forms.TextInput(
                              attrs={
                                  "placeholder":"Input long URL",
                                  "class": "form-control"
                              }
                          ))
    """
    def clean(self):
        cleaned_data = super(SubmitUrlForm, self).clean()
        print(cleaned_data)
        url = cleaned_data.get('url')

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if 'http' in url:
            return url

        return "http://" + url
    """