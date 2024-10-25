def main():
    while True:
        try:
            choice = int(input("1 for adding/updating tasks\n2 for reading tasks\n3 to exit: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        with open("todo.txt", "a+") as fobj:
            if choice == 1:
                x = input("Enter what you want to add: ")
                fobj.writelines(x + "\n")
                print(f"{x} added successfully.")
            elif choice == 2:
                print("Your added tasks are:\n")
                fobj.seek(0)
                tasks = fobj.read()
                print(tasks)
            elif choice == 3:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()