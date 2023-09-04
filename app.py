from userOperations import *
from projectOperations import * 

# Define the main function
def main():
    # Display the welcome message
    print("\nWelcome to the Fundraise Project Console App!")
    print("--------------------------------------------")
    

    # Loop until the user chooses to quit
    while True:
        # Display the main menu and prompt the user for their choice
        print("\n------------------- Main Menu ---------------------\n")
        print("1. Register")
        print("2. Login")
        print("3. Create a project")
        print("4. View all projects")
        print("5. edit a project")
        print("6. delete a project")
        print("7. Search for a project by date")
        print("8. Quit")
        choice = input("Enter the number of your choice: ")

        # Perform the selected action
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            email = input("Enter your email address: ")
            if validate_email(email):
                create_project(email)
        elif choice == "4":
            view_projects()
        elif choice == "5":
            email = input("Enter your email address: ")
            if validate_email(email):
                edit_project(email)
        elif choice == "6":
            email = input("Enter your email address: ")
            if validate_email(email):
                delete_project(email)
        elif choice == "7":
            search_project()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number from 1 to 8.")
            continue

if __name__ == "__main__":
    main()


