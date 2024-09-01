from django import forms
# from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.pop('autofocus', None)
		if 'usable_password' in self.fields:
			del self.fields['usable_password']

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		
    
