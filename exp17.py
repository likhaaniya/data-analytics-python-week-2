def is_palindrome():
    s = input("Enter a string: ").lower().replace(" ", "")
    if s == s[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

is_palindrome()