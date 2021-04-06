# Components, such as libraries, frameworks, and other software modules, run with the same privileges 
# as the application. If a vulnerable component is exploited, such an attack can facilitate serious 
# data loss or server takeover. Applications and APIs using components with known vulnerabilities 
# may undermine application defenses and enable various attacks and impacts.
# (Source)[https://owasp.org/www-project-top-ten/2017/A9_2017-Using_Components_with_Known_Vulnerabilities]

class Using_Components_with_Known_Vulnerabilities():
    def __init__(self, scopeURL, outOfScopeURL):
        self.scopeURL = scopeURL
        self.outOfScopeURL = outOfScopeURL