from conf import settings
import ldap
import ldap.modlist as modlist

def init_bind():
    ld=ldap.initialize(settings.ACCOUNT_LDAP_SERVER_URI)
    ld.simple_bind_s(settings.ACCOUNT_LDAP_BIND_DN,settings.ACCOUNT_LDAP_BIND_PASSWORD)
    return ld

def search(username,ld=None):
    if(ld==None):
        ld=init_bind()
    return ld.search_s(settings.ACCOUNT_LDAP_BASE_DN,settings.ACCOUNT_LDAP_SEARCH_SCOPE,
           "(cn=%s)" % ldap.filter.escape_filter_chars(str(username)))

def searchDenylist(username,ld=None):
    if(ld==None):
        ld=init_bind()
    dn="cn="+str(username)+","+settings.ACCOUNT_LDAP_BASE_DN
    gdn,denylist=__denylist(ld)
    if(dn in denylist["member"]):
        return True
    return False

def appendDenylist(username,ld=None):
    if(ld==None):
        ld=init_bind()
    dn="cn="+str(username)+","+settings.ACCOUNT_LDAP_BASE_DN
    gdn,denylist=__denylist(ld)
    attr=denylist.copy()
    attr["member"]=denylist["member"][:]
    attr["member"].append(dn)
    ldif=modlist.modifyModlist(denylist,attr)
    ld.modify_s(gdn,ldif)

def removeDenylist(username,ld=None):
    if(ld==None):
        ld=init_bind()
    dn="cn="+str(username)+","+settings.ACCOUNT_LDAP_BASE_DN
    gdn,denylist=__denylist(ld)
    attr=denylist.copy()
    attr["member"]=denylist["member"][:]
    attr["member"].remove(dn)
    ldif=modlist.modifyModlist(denylist,attr)
    ld.modify_s(gdn,ldif)

def __denylist(ld):
    result=ld.search_s(settings.ACCOUNT_LDAP_GROUP,settings.ACCOUNT_LDAP_SEARCH_SCOPE,settings.ACCOUNT_LDAP_DENY)
    return result[0]

def save(user):
    attrs={}
    attrs['cn']=str(user.username)
    attrs['objectClass']='inetOrgPerson'
    attrs[settings.ACCOUNT_LDAP_USER_ATTR_MAP["first_name"]]=str(user.first_name)
    attrs[settings.ACCOUNT_LDAP_USER_ATTR_MAP["last_name"]]=str(user.last_name)
    attrs[settings.ACCOUNT_LDAP_USER_ATTR_MAP["email"]]=str(user.email)

    ld=init_bind()
    result=search(user.username,ld)

    dn="cn="+str(user.username)+","+settings.ACCOUNT_LDAP_BASE_DN
    if(result==None or result==[]):
        ldif=modlist.addModlist(attrs)
        ld.add_s(dn,ldif)
    else:
        ldn,data=result[0]
        newData=data.copy()
        for key,attrD in attrs.items():
            newData[key]=attrD
        ldif=modlist.modifyModlist(data,newData)
        ld.modify_s(dn,ldif)

    is_deny=searchDenylist(user.username,ld)
    if(user.is_active==False):
       if(is_deny==False):
           appendDenylist(user.username,ld)
    else:
       if(is_deny==True):
           removeDenylist(user.username,ld)

    ld.unbind()


def changePassword(user,password):
    ld=init_bind()
    result=search(user.username,ld)

    ldn,data=result[0]
    newData=data.copy()
    newData["userPassword"]=str(password)
    ldif=modlist.modifyModlist(data,newData)
    ld.modify_s(ldn,ldif)
    ld.unbind()


def delete(user):
    ld=init_bind()
    dn="cn="+str(user.username)+","+settings.ACCOUNT_LDAP_BASE_DN

    ld.delete(dn)

    ld.unbind()



