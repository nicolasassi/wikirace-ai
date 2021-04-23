from wiki.iterator import WikiPageIterator


class Sentences(object):
    def __init__(self, iterator: WikiPageIterator):
        self._iterator = iterator

    def __iter__(self):
        for it in self._iterator:
            # TODO parse and tokenize text
            yield it
