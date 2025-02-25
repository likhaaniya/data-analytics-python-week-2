import string

def is_pangram():
    s = input("Enter a string: ")
    alphabet = set(string.ascii_lowercase)
    if alphabet <= set(s.lower()):
        print("The string is a pangram.")
    else:
        print("The string is not a pangram.")

is_pangram()
