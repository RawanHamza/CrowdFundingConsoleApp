from userOperations import *
from app import main

# Define function for creating a project
def create_project(email):
    print("\n--------------- Create Project ----------------------\n")
    print("Enter project details:")
    title = input("Enter the title of your project: ")
    details = input("Enter the details of your project: ")
    total_target = input("Enter the total target for your project (in EGP): ")
    start_date = input("Enter the start date of your project (YYYY-MM-DD): ")
    while not validate_date(start_date):
        start_date = input(
            "Invalid date format. Please enter a valid date (YYYY-MM-DD): "
        )
    end_date = input("Enter the end date of your project (YYYY-MM-DD): ")
    while not validate_date(end_date) or end_date <= start_date:
        end_date = input("Invalid date. Please enter a valid end date (YYYY-MM-DD): ")
    project_data = f"{email}:{title}:{details}:{total_target}:{start_date}:{end_date}\n"
    with open("projects.txt", "a") as f:
        f.write(project_data)
    print("Project created successfully.")


# Define function for viewing a project
def view_projects():
    print("\n--------------- View Projects ---------------------\n")
    with open("projects.txt", "r") as f:
        for line in f:
            project_data = line.strip().split(":")
            email = project_data[0]
            title = project_data[1]
            details = project_data[2]
            total_target = project_data[3]
            start_date = project_data[4]
            end_date = project_data[5]
            print(
                f"\n Email: {email}\nTitle: {title}\nDetails: {details}\nTotal target: {total_target}\nStart date: {start_date}\nEnd date: {end_date}\n"
            )



# Define function for editing a project
def edit_project(email):
    print("\n--------------- Edit Projects ---------------------\n")
    project_index = None
    with open("projects.txt", "r") as f:
        projects = f.readlines()
        for i, line in enumerate(projects):
            project_data = line.strip().split(":")
            if email == project_data[0]:
                project_index = i
                break
    if project_index is None:
        print("You have not created any projects.")
        return
    print(f"Select a project to edit (0-{project_index}):")
    for i, line in enumerate(projects[: project_index + 1]):
        project_data = line.strip().split(":")
        title = project_data[1]
        print(f"{i}. {title}")
    selection = input("Enter the number of the project you want to edit: ")
    while (
        not selection.isdigit() or int(selection) < 0 or int(selection) > project_index
    ):
        selection = input(
            f"Invalid input. Please enter a number between 0 and {project_index}: "
        )
    selected_project = projects[int(selection)].strip().split(":")
    title = input("Enter the new title for your project: ")
    details = input("Enter the new details for your project: ")
    total_target = input("Enter the new total target for your project (in EGP): ")
    start_date = input("Enter the new start date for your project: ")
    while not validate_date(start_date):
        start_date = input(
            "Invalid date format. Please enter a valid date (YYYY-MM-DD): "
        )
        end_date = input("Enter the new end date for your project (YYYY-MM-DD): ")
    while not validate_date(end_date) or end_date <= start_date:
        end_date = input("Invalid date. Please enter a valid end date (YYYY-MM-DD): ")
    selected_project[1] = title
    selected_project[2] = details
    selected_project[3] = total_target
    selected_project[4] = start_date
    selected_project[5] = end_date
    projects[int(selection)] = ":".join(selected_project) + "\n"
    with open("projects.txt", "w") as f:
        f.writelines(projects)
    print("Project updated successfully.")




# Define function for deleting a project
def delete_project(email):
    print("\n--------------- Delete Project ---------------------\n")
    project_index = None
    with open("projects.txt", "r") as f:
        projects = f.readlines()
        for i, line in enumerate(projects):
            project_data = line.strip().split(":")
            if email == project_data[0]:
                project_index = i
                break
    if project_index is None:
        print("You have not created any projects.")
        return
    print(f"Select a project to delete (0-{project_index}):")
    for i, line in enumerate(projects[: project_index + 1]):
        project_data = line.strip().split(":")
        title = project_data[1]
        print(f"{i}. {title}")
    selection = input("Enter the number of the project you want to delete: ")
    while (
        not selection.isdigit() or int(selection) < 0 or int(selection) > project_index
    ):
        selection = input(
            f"Invalid input. Please enter a number between 0 and {project_index}: "
        )
    del projects[int(selection)]
    with open("projects.txt", "w") as f:
        f.writelines(projects)
    print("Project deleted successfully.")




# Define function for searching for a project
def search_project():
    print("\n--------------- Search for Projects ----------------\n")
    search_date = input("Enter the date to search for (YYYY-MM-DD): ")
    while not validate_date(search_date):
        search_date = input(
            "Invalid date format. Please enter a valid date (YYYY-MM-DD): "
        )
    with open("projects.txt", "r") as f:
        projects = f.readlines()
    results = []
    for line in projects:
        project_data = line.strip().split(":")
        start_date = project_data[4]
        end_date = project_data[5]
        if start_date <= search_date <= end_date:
            results.append(project_data)
    if not results:
        print("No projects found.")
        return
    print("Search Results:")
    for i, result in enumerate(results):
        title = result[1]
        print(f"{i}. {title}")
    # Prompt the user to select a project to view, edit, or delete
    selected_project_index = input(
        "Enter the index of the project you want to view, edit, or delete (or 'q' to quit): "
    )
    while selected_project_index != "q":
        while not selected_project_index.isdigit() or int(
            selected_project_index
        ) >= len(results):
            selected_project_index = input(
                "Invalid index. Please enter a valid index or 'q' to quit: "
            )
        selected_project = results[int(selected_project_index)]
        selected_project_id = selected_project[0]
        selected_project_title = selected_project[1]

        # Prompt the user to select an action to perform on the selected project
        action = input(
            f"\nSelected project: '{selected_project_title}'. Enter 'v' to view, 'e' to edit, 'd' to delete, or 'q' to quit: "
        )
        while action not in ["v", "e", "d", "q"]:
            action = input(
                "Invalid input. Please enter 'v' to view, 'e' to edit, 'd' to delete, or 'q' to quit: "
            )

        # Perform the selected action on the selected project
        if action == "v":
            view_projects(selected_project_id)
        elif action == "e":
            edit_project(selected_project_id)
        elif action == "d":
            delete_project(selected_project_id)
            results.pop(int(selected_project_index))
            print("Project deleted successfully.")
        else:
            break
        selected_project_index = input(
            "Enter the index of another project to view, edit, or delete (or 'q' to quit): "
        )
    print("Returning to main menu...")
    main()
