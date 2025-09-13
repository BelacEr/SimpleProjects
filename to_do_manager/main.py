import to_do_manager as to_do

while True:
    to_do.show_menu()
    choice = input("Enter your choice:")

    if choice == 1:
        to_do.add_task()
    elif choice == 2:
        to_do.view_task()
    elif choice == 3:
        to_do.mark_task()
    elif choice == 4:
        to_do.delete_task()
    elif choice == 5:
        print("Good bye!")
        break
    else:
        print("Invalid choice. Please try again!")
