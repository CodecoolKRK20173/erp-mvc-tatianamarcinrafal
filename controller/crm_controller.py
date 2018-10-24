# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from controller import common

def run():
    options = ["Add", "Remove", "Update", "Longest name id [in progress]", "Subscribed e-mails[in progress]"]
    common_options = ["Name: ", "E-mail: ", "Newsletter subscribtion[1 - yes/ 0 - no]: "]
    file = "model/crm/customers.csv"
    table = common.get_table_from(file)
    choice = None
    while choice != '0':
        choice = terminal_view.get_choice(options)
        if choice == '1':
            common.add(file, common_options)
        if choice == '2':
            common.remove(file)
        if choice == '3':
            common.update(file, common_options)
        if choice == '4':
            crm.get_longest_name_id(table)
            # print here
        if choice == '5':
            crm.get_subscribed_emails(table)
            # print here

        else:
            terminal_view.print_error_message("There is no such choice.")

