def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark cave.")

def choose_path():
    print("Choose your path:")
    print("1. Go left")
    print("2. Go right")
    choice = input("Enter your choice (1 or 2): ")
    return int(choice)

def explore_left():
    print("You explore the left path and find a treasure chest.")
    print("Do you want to open it? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        print("You open the chest and find a golden key.")
    else:
        print("You decide to leave the chest unopened.")

def explore_right():
    print("You explore the right path and encounter a dragon.")
    print("Do you want to fight it? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        print("You fight the dragon and defeat it.")
    else:
        print("You run away from the dragon.")

def main():
    intro()
    choice = choose_path()

    if choice == 1:
        explore_left()
    elif choice == 2:
        explore_right()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()