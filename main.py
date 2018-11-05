# Do not modify this file
# run this program (the ERP software) from the terminal from thd root directory of this project


import sys
import controller
from view import terminal_view # User Interface
# Store module
from controller import store_controller
# Human Resources module
from controller import hr_controller
# Tool manager module
from controller import inventory_controller
# Accounting module
from controller import accounting_controller
# Sales module
from controller import sales_controller
# Customer Relationship Management (CRM) module
from controller import crm_controller
# Data Analyser module
from data_analyser import data_analyser




def choose():
    choice = None
    while choice != "0":
        choice = handle_menu()
        if choice == "1":
            store_controller.run()
        elif choice == "2":
            hr_controller.run()
        elif choice == "3":
            inventory_controller.run()
        elif choice == "4":
            accounting_controller.run()
        elif choice == "5":
            sales_controller.run()
        elif choice == "6":
            crm_controller.run()
        elif choice == "0":
            terminal_view.print_result("Goodbye")
        else:
            terminal_view.print_error_message("There is no such choice.")

# function after merge
# def choose():
#     inputs = ui.get_inputs(["Please enter a number: "], "")
#     option = inputs[0]
#     if option == "1":
#         store.start_module()
#     elif option == "2":
#         hr.start_module()
#     elif option == "3":
#         inventory.start_module()
#     elif option == "4":
#         accounting.start_module()
#     elif option == "5":
#         sales.start_module()
#     elif option == "6":
#         crm.start_module()
#     elif option == "7":
#         data_analyser.start_module()
#     elif option == "0":
#         sys.exit(0)
#     else:
#             terminal_view.print_error_message("There is no such choice.")


def handle_menu():
    options = ["Store manager",
               "Human resources manager",
               "Inventory manager",
               "Accounting manager",
               "Sales manager",
               "Customer Relationship Management (CRM)"]
    #   ui.print_menu("Main menu", options, "Exit program") < this was here (3 arguments) - may wanna fix that
    return terminal_view.get_choice(options) 


# def main():
#     root_controller.run()


if __name__ == '__main__':
    choose()
