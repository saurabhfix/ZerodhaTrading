from django import forms

class ContactForm(forms.Form):
    auth_token = forms.CharField(max_length=100)


class ArithmeticForm(forms.Form):
    number1 = forms.FloatField(label="First Number", required=True)
    number2 = forms.FloatField(label="Second Number", required=True)

    OPERATION_CHOICES = [
        ('add', 'Addition (+)'),
        ('subtract', 'Subtraction (-)'),
        ('multiply', 'Multiplication (*)'),
        ('divide', 'Division (/)'),
    ]

    operation = forms.ChoiceField(choices=OPERATION_CHOICES, label="Operation", required=True)