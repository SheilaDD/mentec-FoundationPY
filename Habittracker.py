# Habit tracker that allows users to add habits, log their completion, view progress, and visualize it using a bar chart.
# uses a dictionary to store habits and their completion dates, and it provides a menu-driven interface for user interaction.
# Provides feedback based on the user's input.

import datetime  # im importing datetime for date handling
import matplotlib.pyplot as plt  # im importing matplotlib for data visualization

# Dictionary to store habit data, where keys are habit names and values are lists of dates when the habit was completed
habitData = {}


def add_habit():  # This function allows the user to add a new habit to the tracker
    # Convert habit name to lowercase for consistency
    habit = input("Enter the name of the new habit: ").lower()
    # Check if the habit already exists in the habitData dictionary
    if habit in habitData:  # If the habit already exists, notify the user
        # If the habit already exists, notify the user
        print("Habit already exists.")
    else:
        # Initialize the habit with an empty list to store completion dates
        habitData[habit] = []
        # Notify the user that the habit has been added successfully
        print(f"Habit '{habit}' added.")


def log_habit():  # This function allows the user to log the completion of a habit for today
    date = datetime.date.today().isoformat()  # Get today's date (YYYY-MM-DD)
    # .lower Convert habit name to lowercase for consistency
    habit = input("Enter the habit you completed today: ").lower()
    if habit in habitData:  # Check if the habit exists in the habitData dictionary
        # Check if the habit has already been logged for today
        if date not in habitData[habit]:
            # If not logged, append today's date to the habit's list of completion dates
            habitData[habit].append(date)
            # Notify the user that the habit has been logged successfully
            print("Logged successfully!")

        else:
            # If the habit has already been logged for today, notify the user
            print("You've already logged this habit today.")
    else:
        # If the habit does not exist, prompt the user to add it first
        print("Habit not found. Add it first on option 1.")


def view_progress():  # This function displays the progress of all habits tracked
    print("\n Habit Progress:")  # Print a header for the progress report
    if not habitData:  # Check if there are no habits tracked yet
        # If no habits are tracked, notify the user
        print("No habits tracked yet.")
        return  # Return to the main menu if no habits are tracked
    for habit, dates in habitData.items():  # Iterate through each habit and its completion dates
        # Print the habit name (habit.title-capitalized) and the number of days (len(dates)) it has been completed
        print(f"{habit.title()}: {len(dates)} days")


def visualize_progress():  # This function visualizes the progress of habits using a bar chart

    if not habitData:  # Check if there are no habits tracked yet
        # If no habits are tracked, notify the user
        print("No habit data to visualize yet.")
        return  # Return to the main menu if no habits are tracked

    # Get the list of habit names from the habitData dictionary
    habits = list(habitData.keys())
    # Get the count of completion dates for each habit
    # Create a list of counts representing the number of days each habit has been completed
    counts = [len(dates) for dates in habitData.values()]

    plt.bar(habits, counts, color='skyblue')
    plt.title("Habit Completion Count")
    plt.xlabel("Habit")
    plt.ylabel("Days Completed")
    plt.tight_layout()
    plt.show()


def show_menu():  # This function displays the main menu of the habit tracker application
    # Print the menu options for the user to choose from
    print("\n--- The Habit Tracker ---")
    print("1. Add a new habit")
    print("2. Log today's habit")
    print("3. View progress")
    print("4. Visualize progress")
    print("5. Exit")


def main():  # This is the main function that runs the habit tracker application
    while True:
        show_menu()
        # Prompt the user to choose an option from the menu
        choice = input("Choose an option (1-5): ")
        # Based on the user's choice, call the appropriate function

        if choice == "1":  # If the user chooses option 1, call the add_habit function
            add_habit()
        elif choice == "2":  # If the user chooses option 2, call the log_habit function
            log_habit()
        elif choice == "3":  # If the user chooses option 3, call the view_progress function
            view_progress()
        elif choice == "4":  # If the user chooses option 4, call the visualize_progress function
            visualize_progress()
        elif choice == "5":  # If the user chooses option 5, exit the program
            print("Goodbye!")   # Notify the user that the program is exiting
            break
        else:
            print("Invalid choice. Please from  options 1-5.")


if __name__ == "__main__":
    main()


# Done by: Sheila Divhani Dzhivhuho

