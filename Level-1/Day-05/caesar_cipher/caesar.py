text = input("Enter message:").lower()
shift =int(input("Enter shift values:"))

result=""

for char in text:
    if char.isalpha():
        new_char=chr((ord(char)-ord('a')+ shift) % 26 + ord('a'))
        result += new_char
    else:
        result += char

print("Encrypted message:", result)