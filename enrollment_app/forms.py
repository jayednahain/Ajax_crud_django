from django import forms
from enrollment_app.models import User

class UserRegestationForm(forms.ModelForm):
   #email = forms.CharField(widget=forms.Textarea, label='')
   #email =forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailId'}), label='')
   #name=forms.CharField(widget=forms.Textarea, label='')
   #passowrd=forms.CharField(widget=forms.Textarea, label='')
   class Meta:
      model =User
      fields = ['name','email','passowrd','id']

      widgets={
         'name':forms.TextInput(attrs={'class':'form-control','id':'nameId','placeholder':'Enter Name'}),
         'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailId','placeholder':'Enter Email'}),
         'passowrd': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'passwordId','placeholder':'Enter Password'})
      }
      labels={
         'name':'',
         'email':'',
         'passowrd':''

      }


