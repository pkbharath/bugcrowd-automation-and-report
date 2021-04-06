# Security misconfiguration is the most commonly seen issue. This is commonly a result of insecure 
# default configurations, incomplete or ad hoc configurations, open cloud storage, misconfigured 
# HTTP headers, and verbose error messages containing sensitive information. Not only must all 
# operating systems, frameworks, libraries, and applications be securely configured, but they 
# must be patched/upgraded in a timely fashion.
# (Source)[https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration]

class Security_Misconfiguration():
    def __init__(self, scopeURL, outOfScopeURL):
        self.scopeURL = scopeURL
        self.outOfScopeURL = outOfScopeURL