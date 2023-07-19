from django import forms  
from polls.models import User  
class UserForm(forms.ModelForm):  
    class Meta:  
        model = User
        fields = ["id","first_name","last_name","organization"]  