class SiteMapMaker:
    def generate(self, urls):
        result = ""
        result += self.buildHeader()
        for url in urls:
            result += self.buildPage(url)
        result += self.buildFooter()
        return result

    def buildHeader(self):
        return "<ul class=\"sitemap\">\r\n"

    def buildFooter(self):
        return "</ul>\r\n"

    def buildPage(self, url):
        return '\t<li><a href="{0}">{0}</a></li>\r\n'.format(url)
