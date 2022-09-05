from django import forms
from .models import UserReservation


class UserReservationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': "text",
            'name': "name",
            'class': "form-control",
            'id': "name",
            'placeholder': "Your Name",
            'data-rule': "minlen:4",
            'data-msg': "Please enter at least 4 chars",
        })
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'type': "text",
            'name': "phone",
            'class': "form-control",
            'id': "phone",
            'placeholder': "Your Phone",
            'data-rule': "minlen:4",
            'data-msg': "Please enter at least 4 chars",
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'type': "email",
            'name': "email",
            'class': "form-control",
            'id': "email",
            'placeholder': "Your Email",
            'data-rule': "email",
            'data-msg': "Please enter a valid email",
        })
    )
    persons = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'type': "number",
            'name': "people",
            'class': "form-control",
            'id': "people",
            'placeholder': "# of people",
            'data-rule': "minlen:1",
            'data-msg': "Please enter at least 1 chars",
        })
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': "text",
            'name': "date",
            'class': "form-control",
            'id': "date",
            'placeholder': "Date",
            'data-rule': "minlen:4",
            'data-msg': "Please enter at least 4 chars",
        })
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': "text",
            'name': "time",
            'class': "form-control",
            'id': "time",
            'placeholder': "Time",
            'data-rule': "minlen:4",
            'data-msg': "Please enter at least 4 chars",
        })
    )
    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={
            'name': "message",
            'class': "form-control",
            'placeholder': "Message",
            'rows': "5",
        })
    )

    class Meta:
        model = UserReservation
        fields = ('name', 'phone', 'persons', 'message', 'time', 'date', 'email')
