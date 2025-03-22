def area_circle(r):
    return 3.14159 * r**2

if __name__ =='__main__':
    radius = float(input("Enter Radius of the circle: "))
    print(f"The radius of the circle is {radius} & the area of the circle is {area_circle(radius):.2f} Square units.")