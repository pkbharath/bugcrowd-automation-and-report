# Many web applications and APIs do not properly protect sensitive data, 
# such as financial, healthcare, and PII. 
# Attackers may steal or modify such weakly protected data to conduct credit card fraud, identity theft, 
# or other crimes. Sensitive data may be compromised without extra protection, such as encryption 
# at rest or in transit, and requires special precautions when exchanged with the browser.
# (Source)[https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure]

class Sensitive_Data_Exposure():
    def __init__(self, scopeURL, outOfScopeURL):
        self.scopeURL = scopeURL
        self.outOfScopeURL = outOfScopeURL