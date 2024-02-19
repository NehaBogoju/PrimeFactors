import math

def prime_factors(number):
    prime_factors = []
    if number <= 0:
        print("Invalid Input!!")
        return prime_factors

    if number == 1:
        print("Prime factors of", number, "are:")
        return prime_factors

    if number == 2:
        print("Prime factors of", number, "are:")
        prime_factors.append(2)
        return prime_factors

    if number % 2 == 0:
        print("Invalid Input!! Prime number inputs are not allowed")
        return prime_factors

    sqrt_number = math.isqrt(number)
    for potential_factor in range(3, sqrt_number + 1, 2):
        if number % potential_factor == 0:
            prime_factors.append(potential_factor)
            number //= potential_factor
            if number == 1:
                break
    if number > 1:
        prime_factors.append(number)

    return prime_factors

number = int(input("Enter the number: "))
prime_factors_list = prime_factors(number)

if len(prime_factors_list) > 0:
    print("Prime factors of", number, "are:")
    for prime_factor in prime_factors_list:
        print(prime_factor)



