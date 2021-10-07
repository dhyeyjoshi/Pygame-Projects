def test_square_number(square_number):
    for number in square_number:
        count=number*number

    return count

assert test_square_number([2]) == 4
assert test_square_number([8]) == 64
assert test_square_number([10]) == 100
print("YOUR CODE IS CORRECT!")
