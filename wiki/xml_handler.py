import xml.sax


class WikiXMLPageContentHandler(xml.sax.handler.ContentHandler):
    """WikiXMLPageContentHandler extends the behavior of xml.sax.handler.ContentHandler being a content handler
    for Wiki XML data using SAX. It implement the necessary methods for parsing pages and save each parsed page in
    the _page variable as a string"""

    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self._buffer = None
        self._values = {}
        self._current_tag = None
        self._page = None

    @property
    def page(self) -> tuple:
        return self._page

    def reset_page(self):
        self._page = None

    def characters(self, content):
        """Characters between opening and closing tags"""
        if self._current_tag:
            self._buffer.append(content)

    def startElement(self, name: str, attrs: xml.sax.xmlreader.AttributesImpl):
        """Opening tag of element"""
        if name in ('title', 'text'):
            self._current_tag = name
            self._buffer = []

    def endElement(self, name):
        """Closing tag of element"""
        if name == self._current_tag:
            self._values[name] = ' '.join(self._buffer)
        if name == 'page':
            self._page = self._values['text']


class WikiTitleTextHandler(WikiXMLPageContentHandler):
    """WikiTitleTextHandler extends behavior of WikiXMLPageContentHandler and implement the
        necessary methods for parsing pages but saves both title and text of each page in the _page variable as tuple.
        Also ignores pages that starts with #REDIRECT as those seems to have no real content being support pages only.
    """

    def __init__(self):
        super().__init__()

    def endElement(self, name):
        """Closing tag of element"""
        if name == self._current_tag:
            self._values[name] = ' '.join(self._buffer)
        if name == 'page' and not self._values['text'].startswith('#REDIRECT'):
            self._page = (self._values['title'], self._values['text'])
