'''
This module contains functions to do a semantic search on Wikipedia
'''

from pprint import pprint

if __name__ == '__main__':
    print 'Wikipedia Semantic Search'

    import gensim.downloader as api

    # print(api.load("fake-news", return_path=True))

    pprint(api.info())
