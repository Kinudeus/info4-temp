import numpy as np
import pandas as pd
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

    words = re.split(r'\s|\,|\.|\(|\)', arg1.lower())
#    words = m.parse(words)
    counter = Counter(words)
    print(counter)

#    counter = Counter(arg1)
#    print(dict(counter))

wordCount(1)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
