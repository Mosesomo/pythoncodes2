# python program that checks if a number entered is a prime number

def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("{} is  a prime number".format(number))
    else:
        print("{} is a not a prime number".format(number))


n = int(input("Enter the number you need to check: "))
prime_checker(number=n)
