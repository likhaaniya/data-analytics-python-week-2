def is_perfect():
    number = int(input("Enter a number: "))
    if sum(div for div in range(1, number) if number % div == 0) == number:
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")

is_perfect()
