import subprocess
import xml.sax
from wiki.xml_handler import WikiXMLPageContentHandler


class WikiPageIterator:
    def __init__(self, path: str, handler: WikiXMLPageContentHandler):
        self.path = path
        self.handler = handler

    def __iter__(self):
        parser = xml.sax.make_parser()
        parser.setContentHandler(self.handler)
        for line in subprocess.Popen(['bzcat'],
                                     stdin=open(self.path),
                                     stdout=subprocess.PIPE).stdout:
            parser.feed(line)
            # Stop when 3 articles have been found
            if self.handler.page is not None:
                page = self.handler.page
                self.handler.reset_page()
                yield page
