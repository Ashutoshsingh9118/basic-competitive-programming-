# Check if the last digit is divisible by 4

num = int(input("Enter a number: "))

last_digit = num % 10  
if last_digit % 4 == 0:
    print(f"The last digit {last_digit} is divisible by 4.")
else:
    print(f"The last digit {last_digit} is NOT divisible by 4.")