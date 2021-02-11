from django import forms
from .models import User
from django.utils.translation import ugettext_lazy as _

class ProfileForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user')
        super(ProfileForm,self).__init__(*args,**kwargs)

        if not user.is_superuser:
            self.fields['username'].disabled=True
            self.fields['email'].disabled=True
            self.fields['slug'].disabled=True
        self.fields['username'].help_text='نام کاربری خود در هنگام ثبت نام وارد شده و قابل تغییر نیست'
        self.fields['slug'].help_text='کد کاربری کتابخانه ای را از مدیر کتابخانه طلب کنید'

    class Meta:
        model=User
        fields = ['username', 'email', 'first_name', 'last_name', 'slug', 'address']