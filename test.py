
"""""
target_chars = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '{[', ']}',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':;', "@'", '#',
    '|', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<,', '.>',
]

# Define position-specific values
pos_value = {
    # Upper row (0-3, 7-9)
    **{i: 1.032 for i in range(4)},
    **{i: 1.032 for i in range(7, 10)},
    
    # Special characters (4 and 10)
    4: 1.247,  # "t"
    10: 1.247,  # "{["
    
    # "y" (position 5)
    5: 1.605,
    
    # Special character (11)
    11: 1.247,  # "]}"

    # Home row (12-15, 18-21)
    **{i: 0 for i in range(12, 16)},
    **{i: 0 for i in range(18, 22)},
    
    # Lower row (24-27, 29-32)
    **{i: 1.118 for i in range(24, 28)},
    **{i: 1.118 for i in range(29, 33)},
}

# Assign values to characters in target_chars
char_value = {char: pos_value[i] for i, char in enumerate(target_chars)}

# Print the character-value mapping
for char, value in char_value.items():
    print(f"'{char}': {value}")
"""""



target_chars = [ 'q','w','e','r','t','y','u','i','o','p','{[',']}',
                'a','s','d','f','g','h','j','k','l',':;',"@'",'#',
                '|', 'z','x','c','v','b','n','m','<,','.>',]
#0-25

#10-11 {[]}
#21 ;:
pos_value = {
    #0-3 + 7-9 övre
    [0,1,2,3,,7,8,9]: 1.032,
    #pos 4 och 10 "t", "{[" 
    [4,10]: 1.247,
    #pos 5 "y"
    [5]: 1.605,
    #pos 11 "]}"
    [11]: ,
    #Home row 12-15 + 18-21
    [12,13,14,15,18,19,20,21]: 0,
    #lower row 24-27 + 29-32
    [24,25,26,27,29,30,31,32]: 1.118,
    }

x = pos_value.copy()
print (x)