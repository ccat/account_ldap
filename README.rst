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

Installation
============
After installing Django and django-user-accounts, download this from GitHub and save under your project directory.

Modify settings.py as follows;

    ACCOUNT_LDAP_SERVER_URI = "ldap://example.com" #Modify based on your environment
    ACCOUNT_LDAP_BIND_DN = "cn=admin,dc=example,dc=com" #Modify based on your environment
    ACCOUNT_LDAP_BIND_PASSWORD = "secret" #Modify based on your environment
    ACCOUNT_LDAP_BASE_DN="ou=users,dc=example,dc=com" #Modify based on your environment
    ACCOUNT_LDAP_SEARCH_SCOPE=ldap.SCOPE_SUBTREE #Modify based on your environment
    ACCOUNT_LDAP_GROUP="ou=groups,dc=example,dc=com" #Modify based on your environment
    ACCOUNT_LDAP_DENY="cn=disabled" #Modify based on your environment

    ACCOUNT_DELETION_MARK_CALLBACK = "account_ldap.callbacks.account_delete_mark"
    ACCOUNT_DELETION_EXPUNGE_CALLBACK = "account_ldap.callbacks.account_delete_expunge"

    INSTALLED_APPS = [
    ....
    'account_ldap',
    ....
    ]

Modify urls.py as follows;

    urlpatterns = patterns("",
       ....
       url(r"^accounts/", include("account_ldap.urls")),
      ...
    )



解説
============
DjangoのUserデータをLDAPに反映させるためのモジュールです。
django-user-accountsを継承しており、Signup、Settings、Deleteページを用いてUserを更新した時に、
LDAPのデータを更新します。Signalは使用しないため、adminページで更新した場合、LDAPに反映されません。
また、LDAPのobjectClassはinetOrgPersonです。

依存関係
============
* Django
* django-user-accounts

インストール方法
============
Djangoとdjango-user-accountsをインストールした後、GitHubから本モジュールをダウンロードし、
プロジェクト配下に保存してください。

settings.pyに下記を追加してください。
※accountの設定はされているものとします。

    ACCOUNT_LDAP_SERVER_URI = "ldap://example.com" #環境に合わせて修正
    ACCOUNT_LDAP_BIND_DN = "cn=admin,dc=example,dc=com" #環境に合わせて修正
    ACCOUNT_LDAP_BIND_PASSWORD = "secret" #環境に合わせて修正
    ACCOUNT_LDAP_BASE_DN="ou=users,dc=example,dc=com" #環境に合わせて修正
    ACCOUNT_LDAP_SEARCH_SCOPE=ldap.SCOPE_SUBTREE #環境に合わせて修正
    ACCOUNT_LDAP_GROUP="ou=groups,dc=example,dc=com" #環境に合わせて修正
    ACCOUNT_LDAP_DENY="cn=disabled" #環境に合わせて修正

    ACCOUNT_DELETION_MARK_CALLBACK = "account_ldap.callbacks.account_delete_mark"
    ACCOUNT_DELETION_EXPUNGE_CALLBACK = "account_ldap.callbacks.account_delete_expunge"

    INSTALLED_APPS = [
    ....
    'account_ldap',
    ....
    ]

urls.pyに下記を追加してください。

    urlpatterns = patterns("",
       ....
       url(r"^accounts/", include("account_ldap.urls")),
      ...
    )
