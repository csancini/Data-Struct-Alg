import numpy as np


def interleave(one, other):
    """
    Given two messages, A and B, which have the same length,
    creates a new message by taking the first character from A,
    then the first character from B, then the second character
    from A, then the second character from B, and so on.
    """

    inter = ""
    for i in range(len(one)):
        inter = inter + (one[i] + other[i])
    return inter


def fill_dots(message):
    """
    Adds periods (?.?) to the end of the message until its length is a power of 2.
    """
    length = len(message)
    power = int(np.ceil(np.log2(length)))
    return message + ("." * (2**power - length))


def scramble(message):
    """
    Recursively scramble the message by by taking the scramble
    of the first half of the message and the scramble of the second half
    of the message, and interleaving them.
    """
    length = len(message)
    if length == 1:
        return message
    mid = int(length / 2)
    return interleave(scramble(message[:mid]), scramble(message[mid:]))


# loads the messages from the file and fill with dots
lines = [fill_dots(line.rstrip("\n")) for line in open("input.txt")]

# creates a list of scrambled messages
scrambled_message = [scramble(m) for m in lines]

# saves to a file
print(scrambled_message)
file = open("output.txt", "w")
file.write("\n".join(scrambled_message))
file.write("\n")




