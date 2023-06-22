# pip install ldap3

import ldap3
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups

# import logging
# logging.basicConfig(level=logging.DEBUG)
# from ldap3.utils.log import set_library_log_detail_level, get_detail_level_name, set_library_log_hide_sensitive_data, PROTOCOL
# set_library_log_detail_level(PROTOCOL)


def printLdapResult(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        first, rest = args[0], args[1:]
        print(f'{first.l.result}  {func.__name__}{rest}')
    return wrapper


class LdapTest:

    def __init__(self):
        self.ldapSrvIP = '192.168.2.219'  # узнать айпишник
        self.ldapUser = "test\\administrator"
        self.ldapPassword = "Passw0rd"
        self.domainPart = 'DC=test,DC=local'
        self.mainTestOU = 'OU=TestPyOU'
        self.ouClass = ['organizationalUnit', 'top']
        self.userClass = ['organizationalPerson', 'person', 'top', 'user']
        self.groupClass = ['top', 'group']
        self.server = ldap3.Server(self.ldapSrvIP, get_info=ldap3.ALL)
        self.l = ldap3.Connection(self.server, user=self.ldapUser, password=self.ldapPassword, authentication=ldap3.NTLM, auto_bind=True)

    def __del__(self):
        self.l.unbind()

    @printLdapResult
    def createRoot(self):
        self.l.add(f'{self.mainTestOU},{self.domainPart}', self.ouClass)

    @printLdapResult
    def createOU(self, ouName):
        self.l.add(f'OU={ouName},{self.mainTestOU},{self.domainPart}', self.ouClass)

    @printLdapResult
    def createUser(self, userName, dnPart, *attribs):
        self.l.add(f'CN={userName},{dnPart},{self.mainTestOU},{self.domainPart}', self.userClass, *attribs)

    @printLdapResult
    def createGroup(self, groupName, dnPart):
        self.l.add(f'CN={groupName},{dnPart},{self.mainTestOU},{self.domainPart}', self.groupClass)

    @printLdapResult
    def edit(self, dnPart, *conditions):
        self.l.modify(f'{dnPart},{self.mainTestOU},{self.domainPart}', *conditions)

    @printLdapResult
    def addUser2Group(self, userDNPart, groupDNPart):
        ad_add_members_to_groups(self.l,
                                 f"{userDNPart},{self.mainTestOU},{self.domainPart}",
                                 f"{groupDNPart},{self.mainTestOU},{self.domainPart}")

    @printLdapResult
    def delete(self, dnPart):
        self.l.delete(f'{dnPart},{self.mainTestOU},{self.domainPart}')

    @printLdapResult
    def deleteRoot(self):
        self.l.delete(f'{self.mainTestOU},{self.domainPart}')


def testCase1():

    userDict = [
        ["anna1", "OU=nestedOU", {'sn': 'annamaly1', 'givenName': 'Malysheva', 'middleName': 'Sergeevna'}],
        ["annaWithoutMiddleName", "OU=nestedOU", {'sn': 'annamaly2', 'givenName': 'Malysheva'}],
    ]

    test = LdapTest()
    test.createRoot()
    input(f"Root OU was created. Choose {test.mainTestOU},{test.domainPart} as Parent OU for sync. Press Enter to continue...")

    test.createOU("nestedOU")
    test.createGroup("pyGroup", "OU=nestedOU")

    for user in userDict:
        userName, dnPart, attribs = user[0], user[1], user[2]
        test.createUser(userName, dnPart, attribs)
        test.addUser2Group(f'cn={userName},{dnPart}', "cn=pyGroup,OU=nestedOU")

    input("Users were created. Press Enter to continue...")

    test.edit("CN=anna1,OU=nestedOU",
              {'givenName': [(ldap3.MODIFY_REPLACE, ['givenname-1-replaced'])],
               'sn': [(ldap3.MODIFY_REPLACE, ['sn-replaced'])]})

    # удаляем все за собой в обратном порядке, потому что рекурсивного удаления нет
    input("Some users were edited. Press Enter to continue...")

    test.delete("CN=pyGroup,OU=nestedOU")
    for user in userDict:
        userName, dnPart = user[0], user[1]
        test.delete(f'CN={userName},{dnPart}')

    # test.delete("CN=anna1,OU=nestedOU")
    test.delete("OU=nestedOU")
    test.deleteRoot()
    del test


def testCase2():
    test = LdapTest()
    test.l.search('OU=TestPyOU,dc=test,dc=local', '(&(sn=*)(givenName=*)(middleName=*))')
    #print(l.search('dc=test,dc=local', '(objectclass=person)'))
    print(test.l.entries)


testCase1()
