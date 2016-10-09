from django import forms


class DocumentForm(forms.Form):
    docfile = forms.ImageField(
        label='Select a file'
    )
    heading= forms.CharField(required=True)
    footer = forms.CharField(required=True)
