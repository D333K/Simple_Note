import os
import operations

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("Welcome To Simple Note App")
    print('-' * 50)
    print("1. Add Note")
    print("2. Display Notes")
    print("3. Delete Note")
    print("4. Exit")
    print('-' * 50)

    try:
        user_choice = int(input("Enter Your Choice: "))

        if user_choice < 1 or user_choice > 4:
            raise ValueError

    except ValueError:
        print("Enter Valid Number In The Next Time.")
        input("Press Enter To Continue...")
    
    else:
        if user_choice == 1:
            os.system("cls" if os.name == "nt" else "clear")
            print("> 1\n")
            operations.add_note()

            print('-' * 50)
            input("Press Enter To Continue...")

        elif user_choice == 2:
            os.system("cls" if os.name == "nt" else "clear")
            print("> 2\n")
            operations.display_notes()
            
            print('-' * 50)
            input("Press Enter To Continue...")

        elif user_choice == 3:
            os.system("cls" if os.name == "nt" else "clear")
            print("> 3\n")
            operations.delete_note()

            print('-' * 50)
            input("Press Enter To Continue...")


        elif user_choice == 4:
            input("Press Enter To Exit...")
            print("Created By Dark Knight")
            break