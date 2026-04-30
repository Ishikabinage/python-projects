print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose: ")

text = input("Enter message: ").lower()
shift = int(input("Enter shift value: "))

result = ""

for char in text:
    if char.isalpha():
        if choice == "1":
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        result += new_char
    else:
        result += char

print("Result:", result)