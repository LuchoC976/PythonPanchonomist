# String methods

# Strings are a chain of characters (they are not a native data type like int, float, byte, bool)

# Strings in python can be represented using: 'Hello' / "Hello" -> ('...', "...")
# For example: (Both a and b are equal)
string_a = 'Hello'
string_b = "Hello"

# Multiline strings
multiline_str = '''Hello, my name is John
and I work for my dad's 
business!'''

# Every space counts
print(multiline_str)

alphabet_str = "abcdefghijklmnopqrstuvwxyz" # 26
# We can get the length of a string using the len() expression
# For example:
print(len(alphabet_str)) # Len(variable)

# We can search for a specific position in a String using Array notation
# We want to look for the nth element in our string using this notation
# string_name[n], For example: (Starting from 0 to (length - 1))
print("Element 0: " + alphabet_str[0])
print("Element 25: " + alphabet_str[25])
