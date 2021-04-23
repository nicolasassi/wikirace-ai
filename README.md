# Wikipedia race AI

This project aims to be an AI which could play the [Wikipedia race](https://en.wikipedia.org/wiki/Wikipedia:Wiki_Game).
It has all the methods to parse the data from Wikipedia as well as model training and playing the game.

This project have been heavily inspired by the following content:

- [Wikipedia Data Science: Working with the World’s Largest Encyclopedia](https://towardsdatascience.com/wikipedia-data-science-working-with-the-worlds-largest-encyclopedia-c08efbac5f5c)
- [Word Embedding: Word2Vec With Genism, NLTK, and t-SNE Visualization](https://medium.com/swlh/word-embedding-word2vec-with-genism-nltk-and-t-sne-visualization-43eae8ab3e2e)
- [An AI for the Wikipedia Game - Stanford University](http://cs229.stanford.edu/proj2015/309_report.pdf)

### This project is in the very early stages of development, but feel free to contribute :)

## Table of Contents

* [Installation](#installation)
* [Support](#support)
* [License](#license)

## Installation

- Your good old `pip install requirements.txt`
- [Download](https://meta.wikimedia.org/wiki/Data_dump_torrents#English_Wikipedia) the Wikipedia data
- Create an .env file with the following variables:
-
    - DATA_PATH: The local PATH for your enwiki-[DATE-OF-DUMP]-pages-articles-multistream.xml.bz2 file.
- You're good to go ;)

## Support

There are a number of ways you can support the project:

* Use it, star it, build something with it, spread the word!
* Raise issues to improve the project (note: doc typos and clarifications are issues too!)
    - Please search existing issues before opening a new one - it may have already been addressed.
* Pull requests: please discuss new code in an issue first, unless the fix is really trivial.
    - Make sure new code is tested.
    - Be mindful of existing code - PRs that break existing code have a high probability of being declined, unless it
      fixes a serious issue.

## License

The BSD 3-Clause license, very open and free so use whenever you want. Let me know if you build something cool with it!
