from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import *

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'user_type', 'password1', 'password2']
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'
            
            
class AuthForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password1']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'

class PasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            for i_name, i in self.fields.items():
                i.widget.attrs['class'] = 'form-control'           
            
    
class RPForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfileModel
        fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'
            
            
class JSPForm(forms.ModelForm):
    class Meta:
        model = JobseekerProfileModel
        fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'
            
            
class JobpostForm(forms.ModelForm):
    class Meta:
        model = JobpostModel
        fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'
            
class SkillsForm(forms.ModelForm):
    class Meta:
        model = SkillsModel
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'