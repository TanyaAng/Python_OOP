def is_prime(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                return False
        return True


def get_primes(numbers):
    idx = 0
    while idx < len(numbers):
        if is_prime(numbers[idx]):
            yield numbers[idx]
        idx += 1


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
