# from .widgets import DatePickerInput
from django import forms
# from django import crispyforms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Register


class MemberCreationForm(UserCreationForm):
    # birth_date = forms.DateField(widget=DatePickerInput)
    class Meta(UserCreationForm):
        model =Register
        fields = ('username','usertype', 'first_name', 'last_name','gender','birth_date','profile_image')

class DateInput(forms.DateInput):
    input_type = 'date'

class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = Register
        fields = ('username','Usertype', 'first_name', 'last_name','gender','birth_date','profile_image')
        widgets = {

            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
            # 'birth_date': DatePickerInput(),
           
        }

