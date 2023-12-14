#COVID TESTING CODES

assigned_values = {}
n = 65
for i in range(26):
    str_ing = chr(n)
    assigned_values[str_ing] = i 
    n += 1
    i += 1

user_name = input('Name?    ').upper()
keytext = input('Keytext? ').upper()

x = 0
for character in user_name:
    print(character, assigned_values[keytext[x]], chr(ord(character) + assigned_values[keytext[x]]))
    x += 1
