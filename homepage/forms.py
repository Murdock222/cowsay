from django import forms


class MooForm(forms.Form):
    text = forms.CharField(max_length=1000, initial="")