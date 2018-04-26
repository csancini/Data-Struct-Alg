number = 1234567890


def is_prime(num):
    return not [x for x in range(2, num) if num % x == 0]


result = []

n = 1
while n < number:
    print(n)
    n += 1
    if not is_prime(n):
        continue
    div, mod = divmod(number, n)
    if mod:
        continue
    result.append(n)
    number = div

print(result)
