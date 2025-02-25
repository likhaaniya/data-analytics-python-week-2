def sum_of_digits():
    n = abs(int(input("Enter a number: ")))
    print("Sum of digits:", sum(int(digit) for digit in str(n)))

sum_of_digits()
