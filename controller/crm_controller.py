# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from controller import common
from model import data_manager
import os
from time import sleep

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ["Add data", "Remove data", "Update data", "The customer ID with the Longest name", "Newsletter subscribtion", "Customer\'s name with the given ID" ]
    common_options = ["Name: ", "E-mail: ", "Newsletter subscribtion ('1'-yes or '0'-no): "]
    link_for_csv = "model/crm/customers.csv"
    title_list = ["ID", "Name", "E-mail", "Newsletter subscribtion"]
    choice = None
    dont_clear = False  
    while choice != '0':
        if not dont_clear:
            os.system("clear")
            table = data_manager.get_table_from_file(link_for_csv)
            terminal_view.print_table(table, title_list)        
        choice = terminal_view.get_choice_submenu(options)
        dont_clear = False        
        if choice == '1':
            common.add(link_for_csv, common_options)
        elif choice == '2':
            common.remove(link_for_csv)
        elif choice == '3':
            common.update(link_for_csv, common_options)
        elif choice == '4':      
            terminal_view.print_result(crm.get_longest_name_id(table), 'ID of the customer with the Longest name: ')       
            dont_clear = True
        elif choice == '5':
            terminal_view.print_result(crm.get_subscribed_emails(table), 'Customers who has subscribed to the newsletter: ')
            dont_clear = True
        elif choice == '6':
            ID = terminal_view.get_inputs(["ID: "], "Please enter ID: ")
            terminal_view.print_result(crm.get_name_by_id(ID), "Customer\'s name by given ID: ")
            dont_clear = True
        else:
            #os.system("clear")
            terminal_view.print_error_message("There is no such choice, please try again")
            #sleep(1)
            #choice = terminal_view.get_choice_submenu(options) 