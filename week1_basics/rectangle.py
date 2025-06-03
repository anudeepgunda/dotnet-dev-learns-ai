def area_of_rectangle(length,width):
    """Calculate the area of a rectangle."""
    return length * width
def perimeter_of_rectangle(length,width):
    """Calculate the perimeter of a rectangle."""
    return 2 * (length + width)
def main():
    print("Rectangle Calculator")
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    area = area_of_rectangle(length, width)
    perimeter = perimeter_of_rectangle(length, width)
    
    print(f"Area of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")
if __name__ == "__main__":
    main()