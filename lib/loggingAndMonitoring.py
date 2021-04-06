# Insufficient logging and monitoring, coupled with missing or ineffective integration with incident 
# response, allows attackers to further attack systems, maintain persistence, pivot to more systems, 
# and tamper, extract, or destroy data. Most breach studies show time to detect a breach is over 
# 200 days, typically detected by external parties rather than internal processes or monitoring.
# (Source)[https://owasp.org/www-project-top-ten/2017/A10_2017-Insufficient_Logging%2526Monitoring]

class Insufficient_Logging_And_Monitoring():
    def __init__(self, scopeURL, outOfScopeURL):
        self.scopeURL = scopeURL
        self.outOfScopeURL = outOfScopeURL