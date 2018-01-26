------------------ 
About the program
------------------

This program simulates a simple bank. The main job of this program is to keep track of the customers of the bank including all their accounts. 
It also makes it possible to make withdrawals and deposits and transfer money between different accounts.  
The user can also save the data to a file and load data from an existing file.

When adding a new customer to the bank, the program creates an id for them. This id is later used for identifying different customers. 
Likewise, when creating a new account for a customer, the program creates an account number for it. However, the user doesn’t have to 
remember all these ids and account numbers by heart since it’s always possible to print out all the customers including their ids and account numbers.

It’s also good to notice that a customer can have multiple accounts of two types. An account can either be a personal account or a savings account. 
The difference between these two account types is that from a personal account it is possible to make a transfer to any other account but when making 
a transfer from a savings account the owner of the saving account that the money is transfered from must have the same owner as the account that the money
is transfered to.
When creating a new account the balance on the account is automatically set to zero.

Lastly, when saving data to a file, the program creates a file in which all the information is in the right format. 
If the user however wants to create their own file and then load the data, the file should be formatted as followed:

Customer1,id1,account number1,balance
Customer2,id2,account number2,balance

There's also an example file named 'example.txt' in the Bank directory.


----------------------
Compiling the program
----------------------

The program can be compiled in the command prompt with the command 'python main.py'.
After compiling the program, the user will be given all the possible commands and the program will guide them further.
