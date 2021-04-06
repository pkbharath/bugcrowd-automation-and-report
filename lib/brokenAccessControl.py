# Restrictions on what authenticated users are allowed to do are often not properly enforced. 
# Attackers can exploit these flaws to access unauthorized functionality and/or data, 
# such as access other users’ accounts, view sensitive files, modify other users’ data, 
# change access rights, etc.
# (Source)[https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control]

class Broken_Access_Control():
    def __init__(self, scopeURL, outOfScopeURL):
        self.scopeURL = scopeURL
        self.outOfScopeURL = outOfScopeURL