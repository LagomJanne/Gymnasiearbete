
#Hämtar Counter
from collections import Counter
#Räknar alla tecken i en textfil
with open('Test.txt', 'r') as file:
    content = file.read()
print(Counter(content))