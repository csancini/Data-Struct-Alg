def is_hot(number):
    """
    States if a given position is hot (True) or cold state (False)
    """
    if number < 1:
        return True
    return (not is_hot(number / 2)) | (not is_hot(number - 1))


# loads the input file
numbers = [float(line.rstrip("\n")) for line in open("input.txt")]

# identifies if each position is hot or cold
positions = [is_hot(n) for n in numbers]
print(positions)

# saves the result in a file
file = open("output.txt", "w")
for p in positions:
    file.write("hot" if p else "cold")
    file.write("\n")
