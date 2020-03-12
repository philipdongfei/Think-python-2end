from factorial import *
from only_upper import *
from avoids import *
from uses_all import *


print(factorial(5))
t = ['A', 'b', 'C', 'd']
print(only_upper(t))
word = 'apple'
forbidden = 'bc'
required = 'ple'
print(avoids(word, forbidden))
print(uses_all(word, required))
