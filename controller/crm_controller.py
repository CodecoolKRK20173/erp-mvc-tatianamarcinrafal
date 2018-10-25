# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from controller import common
from model import data_manager
import os

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    os.system("clear")
    options = ["Add data", "Remove data", "Update data", "ID of the customer with the Longest name", "Newsletter subscribtion"]
    common_options = ["Name: ", "E-mail: ", "Newsletter subscribtion ('1'-yes or '0'-no): "]
    link_for_csv = "model/crm/customers.csv"
    table = data_manager.get_table_from_file(link_for_csv)
    title_list = ["ID", "Name", "E-mail", "Newsletter subscribtion"]
    choice = None  
    while choice != '0':    
        terminal_view.print_table(table, title_list)        
        choice = terminal_view.get_choice_submenu(options)       
        if choice == '1':
            common.add(link_for_csv, common_options)
        elif choice == '2':
            common.remove(link_for_csv)
        elif choice == '3':
            common.update(link_for_csv, common_options)
        elif choice == '4':
            result = crm.get_longest_name_id(table)
            os.system("clear")         
            terminal_view.print_result(result, 'ID of the customer with the Longest name: ')
            choice = terminal_view.get_choice_submenu(options)          
        elif choice == '5':
            crm.get_subscribed_emails(table)
        else:
            terminal_view.print_error_message("There is no such choice.") 