import numpy as np
import pandas as pd
import doctest
from collections import Counter

def wordCount(arg1):
    arg1 = input('任意の英文を入力してください')
    print(arg1)

    counter = Counter(arg1)
    print(dict(counter))

wordCount(1)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
