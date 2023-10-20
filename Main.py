


#Hämtar Counter
from collections import Counter
#Räknar alla tecken i en textfil
with open('Test.txt', 'r') as file:
    content = file.read()
Content_All = content.lower()

print(Counter(Content_All))



#stagger 1/4 upper, 1/2 lower

#import random


target_chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '{[', ']}',
                'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':;', "@'", '~#',
                '|\\', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<,', '.>','?']

#random.shuffle(target_chars)
#Effort för varje tangent baserat på postitionen i listan ovanför
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

char_to_effort = {}

for i, char in enumerate(target_chars):
    for key, value in pos_value.items():
        if i in key:
            char_to_effort[char] = value

# Print the result
for char, effort in char_to_effort.items():
    print(f"Character '{char}' has effort {effort}")



