import math

def primeNumberChecker(number):
    
    # Check if the number is less than 2
    if number < 2:
        print(f"{number} is not a prime number")
        return

    # Assume the number is prime unless a divisor is found
    isPrime = True

    # Loop from 2 to the square root of the number (inclusive)
    for num in range(2, int(math.sqrt(number)) + 1):
        # If the number is divisible by any num in this range, it is not prime
        if number % num == 0:
            isPrime = False
            break  # Exit the loop if you found a divisor

    # Output the result based on the value of isPrime
    if isPrime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
                     
# Input: Ask the user for the number they want to check
n = int(input("The number you want to check: "))

# Call the function with the input number
primeNumberChecker(n)
