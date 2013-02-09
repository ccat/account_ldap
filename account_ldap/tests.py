"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from account.conf import settings
from django.contrib.auth.models import User
import ldaplib


class ldaplibTest(TestCase):
    def setUp(self):
        user=User()
        user.username="testuser"
        user.first_name="first"
        user.last_name="last"
        ldaplib.delete(user)
        user.username="testuser2"
        ldaplib.delete(user)

    def test_normalusage(self):
        """
        Tests that ldaplib works correctly or not.
        """
        user=User()
        user.username="testuser"
        user.first_name="first"
        user.last_name="last"
        user.email="test@example.com"
        user.is_active=True
        ldaplib.save(user)

        ld=ldaplib.init_bind()
        result=ldaplib.search(user.username,ld)
        self.assertEqual(1,len(result))

        self.assertEqual(False,ldaplib.searchDenylist(user.username,ld))
        ld.unbind()

        password="secret"
        ldaplib.changePassword(user,password)
        user.last_name="lastmod"
        user.email="test@example.com"
        ldaplib.save(user)
        user.is_active=False
        ldaplib.save(user)

        ld=ldaplib.init_bind()
        #result=ldaplib.search(user.username,ld)
        #print(result)
        self.assertEqual(True,ldaplib.searchDenylist(user.username,ld))
        ld.unbind()

        ldaplib.delete(user)

    def test_connErr(self):
        """
        Test when connection is error
        """
        #self.assertEqual(1 + 1, 2)
        try: 
          user=User()
          user.username="testuser2"
          user.first_name="first"
          user.last_name="last"
          user.email="test@example.com"
          tempURI=settings.ACCOUNT_LDAP_SERVER_URI 
          settings.ACCOUNT_LDAP_SERVER_URI="no url"
          self.assertRaises(ldaplib.ldap.LDAPError,ldaplib.save,user)
          password="secret"
          self.assertRaises(ldaplib.ldap.LDAPError,ldaplib.changePassword,user,password)
          self.assertRaises(ldaplib.ldap.LDAPError,ldaplib.delete,user)
        finally:
          settings.ACCOUNT_LDAP_SERVER_URI=tempURI

    def test_itemErr(self):
        """
        Test when something is error
        """
        user=User()
        user.username="testuser2"
        user.first_name="first"
        user.email="test@example.com"
        password="secret"

        self.assertRaises(ldaplib.ldap.LDAPError,ldaplib.save,user)
        self.assertRaises(Exception,ldaplib.changePassword,user,password)

