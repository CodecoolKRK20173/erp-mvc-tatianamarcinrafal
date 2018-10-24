# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common
from controller import root_controller#new

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    
    options = ["Show table","Add data", "Remove data", "Update data", "Go back to Main Menu"]
    
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            terminal_view.print_table(table, title_list)
        elif choice == "2":
            accounting.add(table, record)
        elif choice == "3":
            accounting.remove(table, id_)
        elif choice == "4":
            accounting.update(table, id_, record)
        elif choice == "5":
            root_controller.run()
        elif choice == "6":
            break
        else:
            terminal_view.print_error_message("There is no such choice.")
    # your code
