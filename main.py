'''
*
*Created by Miisa Martio on 21.01.2018.
*
*Copyright © 2018 Miisa Martio. All Rights Reserved.
*
'''

from bank import Bank
import bank_functions

def main():
    
    bank_name = input("Please enter the name of your bank. The first character of the name can't be a space.\n")
    while bank_name == "" or bank_name[0] == " ":
        bank_name = input("Please name the bank correctly.\n")
    bank = Bank(bank_name)
    i = 1
    print("Please enter the number of the action you want to execute next. Here are the choices:\n"
        "1: Add a new customer to the bank.\n2: Remove a customer from the bank.\n"
        "3: Add an account for an existing customer.\n4: Withdraw money from an existing account.\n"
        "5: Deposit money to an existing account.\n"
        "6: Transfer money from an account to another.\n"
        "7: Check the balance in a given account.\n"
        "8: Print out all the customers of the bank including their ids and account numbers."
        "9: Save all existing information (including the customers of the bank "
        "and all their accounts) to a file. Please notice that this stops the program from running.\n"
        "10: Load information from a file.\n11: End the program.")
        
    while i != 8:
        
        i = input()
        
        if i == '1':
            bank_functions.add_customer_to_the_bank(bank)
            
        elif i == '2':
            bank_functions.remove_customer_from_the_bank(bank)
            
        elif i == '3':
            bank_functions.add_an_account_for_a_customer(bank)
            
        elif i == '4':
            bank_functions.withdraw_money(bank)
            
        elif i == '5':
            bank_functions.deposit_money(bank)
            
        elif i == '6':
            bank_functions.transfer_money(bank)
            
        elif i == '7':
            bank_functions.check_balance(bank)
            
        elif i == '8':
            bank_functions.print_information(bank)
            
        elif i == '9':
            bank_functions.save_information(bank)
            break
            
        elif i == '10':
            bank_functions.load_information(bank)
            
        elif i == '11':
            break
            
        else:
            print("Please enter one of the given choices.")
            
        print("Please choose your next action.")
        
    print("The program has ended.")
    

if __name__ == '__main__':
    main()
