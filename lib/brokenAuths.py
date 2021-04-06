# Application functions related to authentication and session management are often implemented incorrectly, 
# allowing attackers to compromise passwords, keys, or session tokens, 
# or to exploit other implementation flaws to assume other users’ identities temporarily or permanently.
# (Source)[https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication]

class Broken_Authentication():
    def __init__(self, scopeURL, outOfScopeURL):
        self.scopeURL = scopeURL
        self.outOfScopeURL = outOfScopeURL