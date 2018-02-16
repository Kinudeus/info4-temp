#/Users/e155705/Work/info4/info4kai
# coding: UTF-8
#https://github.com/Shouma-K/info4-temp

import doctest
from collections import Counter
import re

def wordCount(arg1):
    arg1 = input('任意の英文を入力してください')
    print(arg1)

    word = re.sub('[.],[,]','',arg1.lower())
    words = re.split(r'\s|\,|\.|\(|\)', word.lower()) 
    counter = Counter(words)
    print(counter)

wordCount(1)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
