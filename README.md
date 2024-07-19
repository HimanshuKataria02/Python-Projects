# Banking Management System
Welcome to my Banking Management System project! This Python application simulates basic banking operations using object-oriented programming principles, and I'm excited to share it with you.

## Overview
This project consists of two main classes: Account and Bank.

### Account Class
The Account class represents individual bank accounts. Each account has:

An account number
The account holder's first and last names
A balance
It includes methods to deposit and withdraw funds, and it handles insufficient funds with a custom exception. Static methods are used to manage account number tracking.

### Bank Class
The Bank class is the backbone of the application, managing all banking operations. It initializes by attempting to load account data from a file, ensuring data persistence. Here's what it can do:

Open new accounts
Inquire about account balances
Deposit funds
Withdraw funds
Close accounts
Display all accounts
Each transaction updates the persistent data file to maintain data integrity across sessions.

## Features
Open Account: Create a new account with an initial balance.
Balance Enquiry: Check the balance of an existing account.
Deposit: Add funds to an account.
Withdraw: Remove funds from an account, with insufficient funds protection.
Close Account: Delete an account from the system.
Show All Accounts: Display details of all accounts.
How to Use
Run the main function, and you'll be greeted with a command-line menu to perform various banking operations interactively.

This project is a great demonstration of file handling, exception handling, and object-oriented programming in Python. It's perfect for intermediate Python developers looking to see these concepts in action. I hope you find it useful and insightful!

Feel free to check out the code, and don't hesitate to reach out with any questions or suggestions!

