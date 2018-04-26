# V1
# def position(number):
#     if number < 1:
#         return 1
#
#     a = 1 + position(number / 2)
#     b = 1 + position(number - 1)
#
#     return a % 2 | b % 2


# V2 shorter
def position(number):
    if number < 1:
        return True
    return (not position(number / 2)) | (not position(number - 1))


n = float(input("Enter a game number: "))
pos = position(n)
print("The number", n, "is a", "hot" if pos else "cold", "position")
