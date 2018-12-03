def calc_tri(x, y, z):
    if not isinstance(x, float) or not isinstance(y, float) or not isinstance(z, float):
        print("ja")
        print(type(x))
        return "Invalid input! Please enter a whole number"
    else:
    # calculate the semi-perimeter
        s = float((x + y + z) / 2)
    # calculate the area
        area_tri = (s (s - x) (s - y) (s - z)) * 0.5

    return area_tri


a = float(input("\nPlease input the first number as an integer:"))
b = float(input("Please input the second number as an integer:"))
c = float(input("Please input the third number as an integer:"))

print("\nThe area of your triangle is: %0.1f" % calc_tri(float(a), float(b), float(c)), "m", chr(178), sep="")