from certificates import *


def main():
    certificate = Certificate(subject="International Company A",
                              domainName="company.com")

    print("Price: {}".format(certificate.getPrice()))
    print(certificate.getCsr())

    print("-------")

    wildcard = WildcardCertificate(subject="International Company A",
                                   domainName="company.com")

    print("Price: {}".format(wildcard.getPrice()))
    print(wildcard.getCsr())

    print("-------")

    san = SanCertificate(subject="International Company A",
                         domainName="company.com",
                         alternativeDomains=[
                             "shop.company.com, blog.company.com"])

    print("Price: {}".format(san.getPrice()))
    print(san.getCsr())


if __name__ == "__main__":
    main()
