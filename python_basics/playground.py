def cli_menu():
    while True:
        print("\nMenu:")
        print("1. Say Hello")
        print("2. Show Date")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            print("Hello!")
        elif choice == '2':
            from datetime import datetime
            print(f"Current date and time: {datetime.now()}")
        elif choice == '3':
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
cli_menu()