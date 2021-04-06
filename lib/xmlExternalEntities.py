# Many older or poorly configured XML processors evaluate external entity references within XML 
# documents. External entities can be used to disclose internal files using the file URI handler, 
# internal file shares, internal port scanning, remote code execution, and denial of service attacks.
# (Source)[https://owasp.org/www-project-top-ten/2017/A4_2017-XML_External_Entities_(XXE)]

class XML_External_Entities_XXE():
    def __init__(self, scopeURL, outOfScopeURL):
        self.scopeURL = scopeURL
        self.outOfScopeURL = outOfScopeURL