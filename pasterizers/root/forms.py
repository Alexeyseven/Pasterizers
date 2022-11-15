from django import forms


class ParameterForm(forms.Form):
    CHOICES = [('1', 'First'), ('2', 'Second')]
    day = forms.DateField(widget=forms.SelectDateWidget)
    parameters = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)