import math
from collections import OrderedDict


def merge_the_tools(string, k):
    # your code goes here
    for start in range(0, len(string), k):
        final = start + k
        temp_string = string[start:final]
        temp_string = "".join(OrderedDict.fromkeys(temp_string))
        print(temp_string)


merge_the_tools('AABCAAADAB', 3)



