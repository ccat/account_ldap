from django.conf import settings
from appconf import AppConf
import ldap

class AccountLDAPAppConf(AppConf):
    
    SERVER_URI = "ldap://localhost"
    BIND_DN = "cn=admin,dc=sample"
    BIND_PASSWORD = "secret"
    BASE_DN="ou=users,dc=sample"
    SEARCH_SCOPE=ldap.SCOPE_SUBTREE
    USER_ATTR_MAP = {"first_name": "givenName", "last_name": "sn","email":"mail"}
    GROUP="ou=groups,dc=sample"
    DENY="cn=disabled"
    FIRST_NAME_LABEL='First name'
    FIRST_NAME_INVISIBLE=False
    LAST_NAME_LABEL='Last name'
    LAST_NAME_INVISIBLE=False

