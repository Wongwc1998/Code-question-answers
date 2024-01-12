def square_cutting(n, m):
    """
    Deduction. This question is asking actually asking you about minimum
    values. If you cut a 5x5 from a 7x5 your left with a 5x2. 7-5=2. You can
    only get 2 2x2 squares and 2 1x1 squares by with a 5x2 rectangle.
    5-2 = 3. You have a 3x2 rectangle. 3-2 = 1. You have a 1x2 rectangle,
    then you get two 1x1 squares. Write python code to solve this question.
    """
    squares = []
    while n > 0 and m > 0:
        # Find the smaller of the two dimensions
        smaller = min(n, m)
        # Add the square to the list
        squares.append(f"{smaller}x{smaller}")
        # Update the dimensions
        if n > m:
            n -= smaller
        else:
            m -= smaller
    return squares

if __name__ == "__main__":
    # Test cases
    print(square_cutting(6, 5))
    print(square_cutting(1, 1))
    print(square_cutting(9, 9))
