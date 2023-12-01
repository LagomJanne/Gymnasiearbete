
import pygad
import random
import re
import time
from functools import cache
import argparse
import matplotlib.pyplot as plt

#Hämtar Counter
from collections import Counter
#Räknar alla tecken i en textfil
#with open('datasettest.txt', 'r') as file:
with open('datasettest.txt', 'r') as file:
    content = file.read()
Content_All = content.lower()

print(Counter(Content_All))

#stagger 1/4 upper, 1/2 lower




target_chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[{', ']}',
                'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':;', "@'", '~#',
                '|\\', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<,', '.>','?']
Keyboard_Layout_str = "qwertyuiop[]asdfghjkl;'#\\zxcvbnm,./"
print(Keyboard_Layout_str)

#random.shuffle(target_chars)


#Effort för varje tangent baserat på postitionen i listan ovanför för när fingrarna är på homerow
pos_value = {
    frozenset([0, 1, 2, 3, 7, 8, 9]): 1.032,
    frozenset([4, 10]): 1.247,
    frozenset([5]): 1.605,
    frozenset([11]): 2.236, 
    frozenset([12, 13, 14, 15, 18, 19, 20, 21]): 0,
    frozenset([16,17,22]): 1,
    frozenset([23]): 2,
    frozenset([24, 25, 26, 27, 29, 30, 31, 32]): 1.118,
}
#Räkna ut effort på bokstäver utifrån pos_value
char_to_effort = {}

for i, char in enumerate(target_chars):
    for key, value in pos_value.items():
        if i in key:
            char_to_effort[char] = value

#Skriver ut resultatet
for char, effort in char_to_effort.items():
    print(f"Character '{char}' has effort {effort}")




def init_population(pop_size):
    population = []

    for i in range(pop_size)
        keyboard = random.sample(Keyboard_Layout_str, len(Keyboard_Layout_str))
