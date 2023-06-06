#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

def main():
    # Test case 1: Adding two integers
    a = 10
    b = 5
    result = add_integer(a, b)
    print(f"The sum of {a} and {b} is: {result}")

    # Test case 2: Adding two floating-point numbers
    c = 3.14
    d = 2.5
    result = add_integer(c, d)
    print(f"The sum of {c} and {d} is: {result}")

    # Test case 3: Adding an integer and a floating-point number
    e = 7
    f = 4.5
    result = add_integer(e, f)
    print(f"The sum of {e} and {f} is: {result}")

    # Test case 4: Adding two negative numbers
    g = -6
    h = -3
    result = add_integer(g, h)
    print(f"The sum of {g} and {h} is: {result}")

    # Test case 5: Adding an integer and a string (should raise TypeError)
    i = "abc"
    try:
        result = add_integer(a, i)
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

