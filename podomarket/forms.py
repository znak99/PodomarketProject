from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'line_id', 'address']
    
    def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.line_id = self.cleaned_data['line_id']
        user.address = self.cleaned_data['address']
        user.save()