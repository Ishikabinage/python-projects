text = input("Enter a Sentence or paragraph:\n")

words = text.split()
word_count = len(words)

char_count = len(text)

sentence_count = text.count('.') + text.count('!') + text.count('?')

print("\nResults:")
print(f"words :{word_count}")
print(f"characters:{char_count}")
print(f"Sentences:{sentence_count}")