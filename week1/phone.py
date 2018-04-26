# Write a script that prompts the user for their phone number, x. Then carry out the following steps:
# 1. Compute x minus the sum of the digits of x. Call this result y. (hint: to find the sum of the digits of x,
# check to see what x//10 and x%10 give you)
# 2. Compute the sum of the digits of y, and store the result back in y.
# 3. Repeat step 2 until y has just one digit, then display it.
# What answer do you get?
# x = int(input("Enter your phone:"))

x = 968306868


def sum_number(n):
    sum_n = 0
    new_n = n
    while new_n != 0:
        sum_n += new_n % 10
        new_n = new_n // 10
    return sum_n


y = x - sum_number(x)

while y // 10 != 0:
    y = sum_number(y)
    print(y)

print("ans:", y)