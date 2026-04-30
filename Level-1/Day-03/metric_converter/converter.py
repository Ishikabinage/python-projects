print("Metric conversion tool")

print("\n Choose conversion:")
print("1. Kilometers to meters")
print("2. Kilograms to Grams")
print("3. Celsius to Fahrenheit")

choice = input("Enter Choice(1/2/3):")

if choice == "1":
    km=float(input("Enter kilometers"))
    meters = km * 1000
    print(f"{km} = {meters} m")

elif choice == "2":
    kg = float(input("Enter kilograms"))
    grams = kg*1000
    print(f"{kg} kg = {grams} g")

elif choice =="3":
    c = float(input("Enter Celisus"))
    f = (c*9/5) + 32
    print(f"{c}°C = {f}°F")
else:
    print("Invalid choice!")