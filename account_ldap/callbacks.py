
import ldaplib
from account import callbacks


def account_delete_mark(deletion):
    callbacks.account_delete_mark(deletion)
    ldaplib.save(deletion.user)

def account_delete_expunge(deletion):
    ldaplib.delete(deletion.user)
    callbacks.account_delete_expunge(deletion)
    deletion.user=None

