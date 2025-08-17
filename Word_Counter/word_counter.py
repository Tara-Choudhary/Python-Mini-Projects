print("🔤 Word Counter Tool")
user_input = input("Enter your text: ")

# Count words by splitting text on spaces
words = user_input.split()
num_words = len(words)

# Count characters
num_chars = len(user_input)

# Count sentences (basic: split on '.', '!', '?')
num_sentences = user_input.count(
    '.') + user_input.count('!') + user_input.count('?')
print("Total Words:", num_words)
print("Total Characters:", num_chars)
print("Total Sentences:", num_sentences)
