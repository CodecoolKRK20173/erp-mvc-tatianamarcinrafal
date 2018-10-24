# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
from controller import common


def run():
    options = ["Add", "Remove", "Update", "Lowest price item ID[in progress]", "Items sold between[in progress]"]
    common_options = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
    file = "model/sales/sales.csv"
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
            sales.get_lowest_price_item_id
            # print here
        if choice == '5':
            crm.get_items_sold_between
            # print here

        else:
            terminal_view.print_error_message("There is no such choice.")