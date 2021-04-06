# XSS flaws occur whenever an application includes untrusted data in a new web page without 
# proper validation or escaping, or updates an existing web page with user-supplied data using a 
# browser API that can create HTML or JavaScript. XSS allows attackers to execute scripts in the 
# victim’s browser which can hijack user sessions, deface web sites, or redirect the user to malicious 
# sites.
# (Source)[https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS)]

class Cross_Site_Scripting_XSS():
    def __init__(self, scopeURL, outOfScopeURL):
        self.scopeURL = scopeURL
        self.outOfScopeURL = outOfScopeURL