from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
                widget=forms.TextInput(
        attrs={
            'id'          :'first_name',
            'name'        :'first_name',
            'class'       :'form-control',
            'type'        :"text", 
            'placeholder' : "First name",
        }
    )
)
    last_name = forms.CharField(max_length=30, required=False,
            widget=forms.TextInput(
        attrs={
            'id'          :'last_name',
            'name'        :'last_name',
            'class'       :'form-control',
            'type'        :"text", 
            'placeholder' : "Last name",
        }
    ))
    
    email = forms.EmailField(max_length=254,required=True,
        widget=forms.EmailInput(
        attrs={
            'id'          :'email',
            'name'        :'email',
            'class'       :'form-control',
            'type'        :"email", 
            'placeholder' : "Email address",
        }
    ))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm the password'
