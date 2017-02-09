class Certificate:
    def __init__(self, subject, domainName):
        if "*" in domainName:
            raise Exception("Order WildcardCertificate")
        self.domainName = domainName
        self.subject = subject

    def getPrice(self):
        return 50

    def getCsr(self):
        return "CSR: \r\n" \
               "Subject : {}\r\n" \
               "domainName: {}".format(self.subject, self.domainName)


class WildcardCertificate(Certificate):
    def __init__(self, subject, domainName):
        super(WildcardCertificate, self).__init__(subject, domainName)
        self.domainName = "*." + self.domainName

    def getPrice(self):
        return super(WildcardCertificate, self).getPrice() + 20

    def getCsr(self):
        return "{}\r\n" \
               "wildcard: yes".format(
            super(WildcardCertificate, self).getCsr())


class SanCertificate(Certificate):
    def __init__(self, subject, domainName, alternativeDomains):
        super(SanCertificate, self).__init__(subject, domainName)
        self.alternativeDomains = alternativeDomains

    def getPrice(self):
        return super(SanCertificate, self).getPrice() + 30

    def getCsr(self):
        return "{}\r\n" \
               "Subject Alternative Names: {}".format(
            super(SanCertificate, self).getCsr(), self.alternativeDomains)
