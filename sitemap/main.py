from makers import *


def main():
    maker = SiteMapMaker()
    print(maker.generate([
        "http://example.com/contact",
        "http://example.com/home",
        "http://example.com/about us"
    ]))

if __name__ == "__main__":
    main()
