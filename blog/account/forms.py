from django import forms
from django.contrib.auth.models import User
from account.models import UserProfile


class UserForm(forms.ModelForm):
    username = forms.CharField(label='帳號')
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'password')
        
    def clean(self):
        cleanedData = self.cleaned_data
        password = cleanedData.get('password')
        password2 = cleanedData.get('password2')
        if password and password2 and password!=password2:
            raise forms.ValidationError('密碼不相符')
        return cleanedData
    
    
class UserProfileForm(forms.ModelForm):
    fullName = forms.CharField(label='姓名', max_length=128)
    website = forms.URLField(label='個人網址')
    address = forms.CharField(label='住址', max_length=128)
    
    class Meta:
        model = UserProfile
        fields = ('fullName', 'website', 'address')