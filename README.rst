==============================================
account_ldap: LDAP expansion for Django account
==============================================

Description
============
This is a module that reflects Django User data to LDAP.
This inherits django-user-accounts, and when User data is changed by Signup, Settings or Delete page,
LDAP data is updated.  Signals are not used, so LDAP data is not updated when User updated by admin page.
Also, objectClass of LDAP is inetOrgPerson.

Requirements
============
* Django
* django-user-accounts
