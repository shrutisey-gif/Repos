# String Commands

text = " Python Learning "

# 1. Strip: Removes leading and trailing whitespace
text_stripped = text.strip()
print(f"Original: '{text}' | Stripped: '{text_stripped}'")

# 2. Lowercase: Converts all characters to lower case
print(f"Lowercase: '{text_stripped.lower()}'")

# 3. Uppercase: Converts all characters to upper case
print(f"Uppercase: '{text_stripped.upper()}'")

# 4. Replace: Substitutes a substring with a new value
print(f"Replaced: '{text_stripped.replace('Learning', 'Programming')}'")

# 5. Split: Converts a string into a list of strings based on a delimiter
print(f"Split into list: '{text_stripped.split(' ')}'")

# 6. Starts With: Checks if a string begins with specific text (Returns True/False)
print(f"Starts with 'Python'?: {text_stripped.startswith('Python')}")

# 7. Find: Locates the index position of a substring (-1 if not found)
print(f"Index position of 'Python': {text_stripped.find('Python')}")