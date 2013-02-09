import re

from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib import auth
from django.contrib.auth.models import User

from conf import settings
#from account.models import EmailAddress

#from account.ldaplib import changeLdapPassword
from account.forms import SignupForm as accountSignupForm
from account.forms import SettingsForm as accountSettingsForm

alnum_re = re.compile(r"^\w+$")

class SignupForm(accountSignupForm):

    if(settings.ACCOUNT_LDAP_FIRST_NAME_INVISIBLE==False):
        first_name = forms.CharField(
            label=_(settings.ACCOUNT_LDAP_FIRST_NAME_LABEL), 
            max_length=30,
            widget=forms.TextInput(),
            required=True
        )
    if(settings.ACCOUNT_LDAP_LAST_NAME_INVISIBLE==False):
        last_name = forms.CharField(
            label=_(settings.ACCOUNT_LDAP_LAST_NAME_LABEL), 
            max_length=30, 
            widget=forms.TextInput(),
            required=True,
            #initial='NONE'
        )
    
    def clean_first_name(self):
        if("first_name" not in self.cleaned_data):
            return "NONE"
        if not alnum_re.search(self.cleaned_data["first_name"]):
            raise forms.ValidationError(_("Nickname can only contain letters, numbers and underscores."))
        return self.cleaned_data["first_name"]

    def clean_last_name(self):
        if("last_name" not in self.cleaned_data):
            return "NONE"
        if not alnum_re.search(self.cleaned_data["last_name"]):
            raise forms.ValidationError(_("Second Nickname can only contain letters, numbers and underscores."))
        return self.cleaned_data["last_name"]
    
class SettingsForm(accountSettingsForm):

    if(settings.ACCOUNT_LDAP_FIRST_NAME_INVISIBLE==False):
        first_name = forms.CharField(
            label=_(settings.ACCOUNT_LDAP_FIRST_NAME_LABEL), 
            max_length=30,
            widget=forms.TextInput(),
            required=True
        )
    if(settings.ACCOUNT_LDAP_LAST_NAME_INVISIBLE==False):
        last_name = forms.CharField(
            label=_(settings.ACCOUNT_LDAP_LAST_NAME_LABEL), 
            max_length=30, 
            widget=forms.TextInput(),
            required=True,
            #initial='NONE'
        )
    
    def clean_first_name(self):
        if("first_name" not in self.cleaned_data):
            return "NONE"
        if not alnum_re.search(self.cleaned_data["first_name"]):
            raise forms.ValidationError(_("Nickname can only contain letters, numbers and underscores."))
        return self.cleaned_data["first_name"]

    def clean_last_name(self):
        if("last_name" not in self.cleaned_data):
            return "NONE"
        if not alnum_re.search(self.cleaned_data["last_name"]):
            raise forms.ValidationError(_("Second Nickname can only contain letters, numbers and underscores."))
        return self.cleaned_data["last_name"]

