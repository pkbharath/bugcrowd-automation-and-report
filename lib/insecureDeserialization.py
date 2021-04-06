# Insecure deserialization often leads to remote code execution. Even if deserialization flaws do 
# not result in remote code execution, they can be used to perform attacks, including replay attacks, 
# injection attacks, and privilege escalation attacks.
# (Source)[https://owasp.org/www-project-top-ten/2017/A8_2017-Insecure_Deserialization]

class Insecure_Deserialization():
    def __init__(self, scopeURL, outOfScopeURL):
        self.scopeURL = scopeURL
        self.outOfScopeURL = outOfScopeURL