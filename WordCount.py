#/Users/e155705/Work/info4/info4kai
# coding: UTF-8
#https://github.com/Shouma-K/info4-temp

import doctest
from collections import Counter
import MeCab
import re 

def wordCount(arg1):
    arg1 = input('任意の英文を入力してください')
    print(arg1)

#    m = MeCab.Tagger()
#    print(m.parse(arg1))
#    print(m.Counter(arg1))

#    words = re.split(r'\s|\,|\.|\(|\|)', arg1.lower())
    word = re.sub('[.],[,]','',arg1.lower())
    words = re.split(r'\s|\,|\.|\(|\)', word.lower()) 
#    words = re.split(r'\s|\,|\.|\(|\)', arg1.lower())
 #   mecabWords = m.parse(words)
    counter = Counter(words)
    print(counter)
#    counter = Counter(arg1)
#    print(dict(counter))


wordCount(1)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
