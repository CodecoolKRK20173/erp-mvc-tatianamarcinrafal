# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from controller import common
from model import data_manager
import os

def run():
    title_list = ["ID", "Name", "E-mail", "Newsletter subscribtion"]
    options = ["Show table","Add data", "Remove data", "Update data", "ID of the customer with the Longest name", "Newsletter subscribtion"]
    #common_options = ["Name: ", "E-mail: ", "Newsletter subscribtion ('1'-yes or '0'-no): "]
    link_for_csv = "model/crm/customers.csv"
    choice = None
    while choice != '0':
        choice = terminal_view.get_choice(options)
        if choice == '1':
            os.system("clear")
            table = data_manager.get_table_from_file(link_for_csv)    
            terminal_view.print_table(table, title_list)
        elif choice == '2':
            add()
        elif choice == '3':
            remove()
        elif choice == '4':
            update()
        elif choice == '5':
            crm.get_longest_name_id(table)
        elif choice == '6':
            crm.get_subscribed_emails(table)
        else:
            terminal_view.print_error_message("There is no such choice.")

def add():
    link_for_csv = "model/crm/customers.csv"
    table = data_manager.get_table_from_file(link_for_csv)
    title_list = ["Name: ", "E-mail: ", "Newsletter subscribtion ('1'-yes or '0'-no): "]
    record = terminal_view.get_inputs(title_list, "Please provide following data:")
    crm.add(table, record)
    data_manager.write_table_to_file(link_for_csv, table)

def remove():
    link_for_csv = "model/crm/customers.csv"
    table = data_manager.get_table_from_file(link_for_csv)
    id_ = terminal_view.get_inputs(["ID: "], "Please provide ID you want to remove")
    crm.remove(table, id_)
    data_manager.write_table_to_file(link_for_csv, table)

def update():
    link_for_csv = "model/crm/customers.csv"
    table = data_manager.get_table_from_file(link_for_csv)
    id_ = terminal_view.get_inputs(["ID: "], "Please provide ID you want to edit")
    title_list = ["Name: ", "Day: ", "E-mail: ", "Newsletter subscribtion ('1'-yes or '0'-no): "]
    record = terminal_view.get_inputs(title_list, "Please provide following data:")
    crm.update(table, id_, record)
    data_manager.write_table_to_file(link_for_csv, table)
