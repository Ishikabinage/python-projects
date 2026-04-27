while True:
    year = int(input("Enter a year(or 0 to exit):"))

    if year == 0:
        break

    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        print("leap year")
    else:
        print("Not Leap Year")