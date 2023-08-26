import collections
from collections import OrderedDict, defaultdict, Counter, namedtuple, deque
from typing import Final

digits = [1,2,3]
def plusOne(digits):
    digits = [str(i) for i in digits]
    digits = int(''.join(digits))
    digits += 1
    digits = [int(i) for i in str(digits)]
    return digits