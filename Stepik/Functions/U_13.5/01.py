def is_valid_triangle(side1, side2, side3):
    return side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2

a, b, c = int(input('Длиннa')), int(input('Длиннa')), int(input('Длиннa'))

print(is_valid_triangle(a, b, c))