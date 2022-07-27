from django import forms
from .models import User

# Create form named UserForm
class UserForm(forms.Form):
    user_field = forms.IntegerField(max_length = 200)

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'tag_along',
]
