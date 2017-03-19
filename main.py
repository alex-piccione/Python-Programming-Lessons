
# Solution #

def high_and_low(numbers):
    # ...
    return numbers



# Tests #

assert high_and_low("1 -1") == [1, -1]
assert high_and_low("-1 -1") == [-1, -1]
assert high_and_low("1 1") == [1, 1]
assert high_and_low("1 -1 0") == [1, -1]
assert high_and_low("1 1 0") == [1, 0]
assert high_and_low("42") == [42, 42]
assert high_and_low("-1 -1 0") == [0, -1]
assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == [542, -214]

