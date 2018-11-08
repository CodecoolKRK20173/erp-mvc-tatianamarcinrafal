from view import terminal_view

from model.sales import sales
from data_analyser import data_analyser
from controller import common
from model import data_manager
import os



def run():
    options = ["Customer name of the last buyer",
                "Customer ID of the last buyer", 
                "Customer who spent the most money", 
                "Customer\'s ID who spent the most money", 
                "Buyers, who effected more purchases", 
                "Buyers\' ID, who effected more purchases"]
    choice = None
    terminal_clear = False
    while choice != '0':
        if not terminal_clear:
            os.system("clear")
            # table = common.clear_instructions(file, title_list)
        choice = terminal_view.get_choice_submenu(options)
        terminal_clear = False
        if choice == '1':
            last_buyer = data_analyser.get_the_last_buyer_name()
            terminal_view.print_result(last_buyer, 'Customer name of the last buyer: ')
            terminal_clear = True
        elif choice == '2':
            last_buyer_id = data_analyser.get_the_last_buyer_id()
            terminal_view.print_result(last_buyer_id, 'Customer ID of the last buyer: ')
            terminal_clear = True
        elif choice == '3':
            customer_most_money = data_analyser.get_the_buyer_name_spent_most_and_the_money_spent()
            terminal_view.print_result(customer_most_money, "Customer who spent the most money: ")
            terminal_clear = True
        elif choice == '4':
            customer_id_most_money = data_analyser.get_the_buyer_id_spent_most_and_the_money_spent()
            terminal_view.print_result(customer_id_most_money, "Customer\'s ID who spent the most money: ")
            terminal_clear = True
        elif choice == '5':
            num = int(terminal_view.get_input("Number of people: ","Please enter a number of people, who you want to see, in the list of more purchases: "))
            list_buyers_sales = data_analyser.get_the_most_frequent_buyers_names(num)
            terminal_view.print_result(list_buyers_sales, "Buyers, who effected more purchases: ")
            terminal_clear = True
        elif choice == '6':
            num = int(terminal_view.get_input("Number of people: ", "Please enter a number of people, who you want to see, in the list of more purchases: "))
            list_id_buyers_sales = data_analyser.get_the_most_frequent_buyers_ids(num)
            terminal_view.print_result(list_id_buyers_sales, "Buyers\' ID, who effected more purchases: ")
            terminal_clear = True
        else:
            terminal_view.print_error_message("There is no such choice, please try again")
