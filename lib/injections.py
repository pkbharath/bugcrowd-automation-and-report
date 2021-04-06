# Injection flaws, such as SQL, NoSQL, OS, and LDAP injection, 
# occur when untrusted data is sent to an interpreter as part of a command or query. 
# The attacker’s hostile data can trick the interpreter into executing unintended commands 
# or accessing data without proper authorization.
# (Source)[https://owasp.org/www-project-top-ten/2017/A1_2017-Injection]

class Injection():
    def __init__(self, scopeURL, outOfScopeURL):
        self.scopeURL = scopeURL
        self.outOfScopeURL = outOfScopeURL