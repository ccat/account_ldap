# Create your views here.

import ldaplib
from account.views import SignupView as accountSignup
from account.views import ChangePasswordView as accountChangePassword
from account.views import PasswordResetTokenView as accountPasswordResetToken
from account.views import SettingsView as accountSettings
#from account.views import DeleteView as accountDelete
from forms import SignupForm, SettingsForm

from conf import settings

class SignupView(accountSignup):
    form_class = SignupForm

    def form_valid(self, form):
        result=super(SignupView,self).form_valid(form)
        password = form.cleaned_data.get("password")
        ldaplib.save(self.created_user)
        ldaplib.changePassword(self.created_user,password)
        #raise Exception(result)
        return result

    def create_user(self, form, commit=True, **kwargs):
        user=super(SignupView,self).create_user(form,commit,**kwargs)
        #user.first_name = form.cleaned_data["first_name"]
        #user.last_name = form.cleaned_data["last_name"]
        user.first_name = form.clean_first_name()
        user.last_name = form.clean_last_name()

        password = form.cleaned_data.get("password")
        if commit:
            user.save()
            ldaplib.save(user)
            if(password):
                 ldaplib.changePassword(user,password)
        #raise Exception(user.first_name,user.last_name)
        return user

class ChangePasswordView(accountChangePassword):
    def change_password(self, form):
        super(ChangePasswordView,self).change_password(form)
        password = form.cleaned_data["password_new"]
        ldaplib.changePassword(self.request.user,password)
    
class PasswordResetTokenView(accountPasswordResetToken):
    def form_valid(self, form):
        result=super(PasswordResetTokenView,self).form_valid(form)
        user = self.get_user()
        ldaplib.changePassword(user, form.cleaned_data["password"])
        return result

class SettingsView(accountSettings):
    form_class = SettingsForm

    def update_settings(self, form):
        super(SettingsView,self).update_settings(form)
        user = self.request.user
        user.first_name = form.clean_first_name()
        user.last_name = form.clean_last_name()
        user.save()
        ldaplib.save(user)

    def get_initial(self):
        initial = super(SettingsView, self).get_initial()
        if(settings.ACCOUNT_LDAP_FIRST_NAME_INVISIBLE==False):
            initial["first_name"] = self.request.user.first_name
        if(settings.ACCOUNT_LDAP_LAST_NAME_INVISIBLE==False):
            initial["last_name"] = self.request.user.last_name

        return initial

#class DeleteView(accountDelete):


