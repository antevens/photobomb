from django import forms


class DocumentForm(forms.Form):
    docfile = forms.ImageField(
        label='Select a file'
    )
    heading = forms.CharField(required=True, label='Heading for Image', initial='Figure 1 ....')
    footer = forms.CharField(required=True, label='Footer for Image', initial='Source .....')
