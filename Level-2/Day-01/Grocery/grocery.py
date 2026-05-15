grocery = []

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

    choice = input("choice:")

    if choice == "1":
        item = input("Enter item:")
        grocery.append(item)

    elif choice == "2":
        item = input("Enter item to remove:")

        if item in grocery:
            grocery.remove(item)
            print("Removed!")
        else:
            print("item not found")


    elif choice == "3":
        print(grocery)

    elif choice == "4":
        break