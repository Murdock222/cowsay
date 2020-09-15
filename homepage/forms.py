from django import forms


class MooForm(forms.Form):
    text = forms.CharField(max_length=50, initial="")