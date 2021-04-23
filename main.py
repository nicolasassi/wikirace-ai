from wiki.xml_handler import WikiTitleTextHandler
from wiki.iterator import WikiPageIterator
from sentences import Sentences
import settings

if __name__ == '__main__':
    handler = WikiTitleTextHandler()
    it = WikiPageIterator(settings.DATA_PATH, handler)
    cntr = 0
    for sentence in Sentences(it):
        print(sentence)
        cntr += 1
        if cntr == 1:
            break
