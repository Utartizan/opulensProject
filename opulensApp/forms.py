from django import forms # type: ignore

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=101)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    # Custom validation to ensure passwords match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class EmailOrUsernameLoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=101, label='Username or email')
    password = forms.CharField(widget=forms.PasswordInput)
