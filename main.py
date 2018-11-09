

import sys
import controller
from view import terminal_view  # User Interface
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
from controller import analyser_controller


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
        elif choice == "7":
            analyser_controller.run()
        elif choice == "0":
            terminal_view.print_result("Goodbye")
        else:
            terminal_view.print_error_message("There is no such choice.")


def handle_menu():
    options = ["Store manager",
               "Human resources manager",
               "Inventory manager",
               "Accounting manager",
               "Sales manager",
               "Customer Relationship Management (CRM)",
               "Data analyser"]
    return terminal_view.get_choice(options)

if __name__ == '__main__':
    choose()
