def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            shopping_list += [(input("Enter the item to add: "))] # Prompt for and add an item
            pass
        elif choice == '2':
            shopping_list.remove(input('Enter the item to be remove: ')) # Prompt for and remove an item
            pass
        elif choice == '3':
            print(shopping_list) # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()