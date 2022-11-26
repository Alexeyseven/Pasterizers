from django import forms


class ParameterForm(forms.Form):
    CHOICES = [
    ('temp_past', 'Температура в камере пастеризации'),
    ('press_past', 'Давление в камере пастеризации'),
    ('temp_cool', 'Температура охлаждения'),
    ('pu', 'Коэффициент пастеризации'),
    ('o2', 'Показания кислородомера'),
    ('flow', 'Поток')
    ]
    CHOICES_hour = [('0', '0'),
                    ('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4'),
                    ('5', '5'),
                    ('6', '6'),
                    ('7', '7'),
                    ('8', '8'),
                    ('9', '9'),
                    ('10', '10'),
                    ('11', '11'),
                    ('12', '12'),
                    ('13', '13'),
                    ('14', '14'),
                    ('15', '15'),
                    ('16', '16'),
                    ('17', '17'),
                    ('18', '18'),
                    ('19', '19'),
                    ('20', '20'),
                    ('21', '21'),
                    ('22', '22'),
                    ('23', '23'),]
    day = forms.DateField(widget=forms.SelectDateWidget)
    parameters = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=CHOICES,
        required=False,)
    hour_from = forms.ChoiceField(
        choices=CHOICES_hour,
        required=False) 
    hour_to = forms.ChoiceField(
        choices=CHOICES_hour,
        required=False)       
