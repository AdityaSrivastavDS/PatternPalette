# pattern_generator.py

def star_pattern(n):
    """Generate a star pattern of size n."""
    print("Star Pattern:")
    for i in range(n):
        print('*' * (i + 1))
    for i in range(n - 1, 0, -1):
        print('*' * i)
    print()

def number_pattern(n):
    """Generate a number pattern of size n."""
    print("Number Pattern:")
    for i in range(1, n + 1):
        print(' '.join(str(j) for j in range(1, i + 1)))
    print()

def grid_pattern(rows, cols):
    """Generate a grid pattern with the given number of rows and columns."""
    print("Grid Pattern:")
    for i in range(rows):
        print('+ ' * cols)
        print('- ' * cols)
    print()

def pyramid_pattern(n):
    """Generate a pyramid pattern of stars."""
    print("Pyramid Pattern:")
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    print()

def inverted_pyramid_pattern(n):
    """Generate an inverted pyramid pattern of stars."""
    print("Inverted Pyramid Pattern:")
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    print()

def diamond_pattern(n):
    """Generate a diamond pattern of stars."""
    print("Diamond Pattern:")
    # Upper part
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    # Lower part
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    print()

def right_angle_triangle_pattern(n):
    """Generate a right-angle triangle pattern of stars."""
    print("Right-Angle Triangle Pattern:")
    for i in range(1, n + 1):
        print('*' * i)
    print()

def hollow_square_pattern(n):
    """Generate a hollow square pattern with stars."""
    print("Hollow Square Pattern:")
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')
    print()

def fibonacci_pattern(n):
    """Generate a pattern of Fibonacci numbers."""
    print("Fibonacci Pattern:")
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

def number_pyramid_pattern(n):
    """Generate a number pyramid pattern."""
    print("Number Pyramid Pattern:")
    for i in range(1, n + 1):
        print(' ' * (n - i) + ' '.join(str(j) for j in range(1, i + 1)))
    print()

def hollow_diamond_pattern(n):
    """Generate a hollow diamond pattern of stars."""
    print("Hollow Diamond Pattern:")
    # Upper part
    for i in range(n):
        print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i != 0 else ''))
    # Lower part
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i != 0 else ''))
    print()

if __name__ == "__main__":
    star_pattern(5)
    number_pattern(5)
    grid_pattern(4, 5)
    pyramid_pattern(5)
    inverted_pyramid_pattern(5)
    diamond_pattern(5)
    right_angle_triangle_pattern(5)
    hollow_square_pattern(5)
    fibonacci_pattern(10)
    number_pyramid_pattern(5)
    hollow_diamond_pattern(5)
