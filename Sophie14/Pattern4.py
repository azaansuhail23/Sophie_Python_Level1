char = "A"
ascii_value = ord(char)
print(f"ASCII value of {char} is {ascii_value}")  # Output: ASCII value of A is 65

char_B="B"
print(ord(char_B))

print("---------")

for row in range(6):
    letter='A'
    for col in range(row):
        print(letter,end="")
        
        letter = chr(ord(letter)+1)
    print("\n")
