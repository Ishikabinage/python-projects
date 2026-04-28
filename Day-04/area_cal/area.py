print("Area Calculator")

print("\n Choose shape:")
print("1.Rectangle")
print("2.Circle")
print("3.Triangle")

choice = input("Enter choice(1/2/3):")

if choice == "1" :
    length = float(input("Enter Length:"))
    width = float(input("Enter Width:"))
    area = length * width
    print(f"Area of Rectangle ={area}")

elif choice == "2":
    radius = float(input("Enter radius:"))
    area= 3.14 *radius*radius
    print(f"Area of Circle={area}")

elif choice =="3":
    base=float(input("Enter base:"))
    height = float(input("Enter height:"))
    area = 0.5 * base* height
    print(f"Area of triangle = {area}")

else:
    print("Invalid choice!")