import random

#Hämtar Counter
from collections import Counter
#Räknar alla tecken i en textfil
with open('Test.txt', 'r') as file:
    content = file.read()
Content_All = content.lower()

print(Counter(Content_All))


#Värden för tangenter, 0, 1, 1.038, 1.118, 2.138, 1.247, 1.605, 1.803, 2.661, 2.015


target_chars = [ 'q','w','e','r','t','y','u','i','o','p','{[',']}',
                'a','s','d','f','g','h','j','k','l',':;',"@'",'#',
                '', 'z','x','c','v','b','n','m','<,','.>',]
#0-25

#10-11 {[]}
#21 ;:
pos_value = {
    #0-4 + 7-9 övre
    [0,1,2,3,4,7,8,9]: 1.032,
    #pos 5 "t" 
    [5]: 1.247,
    #pos 6 "y"
    [6]: 1.605,
    #Home row 12-15 + 18-21
    [12,13,14,15,18,19,20,21]: 0,
    #lower row 24-27 + 29-32
    [24,25,26,27,29,30,31,32]: 1.118,
    
}
