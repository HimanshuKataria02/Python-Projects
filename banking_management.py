class InsufficientFunds(Exception):
    pass

class Account:
    NextAccountNumber = 0

    def __init__(self, fname="", lname="", balance=0.0):
        Account.NextAccountNumber += 1
        self.accountNumber = Account.NextAccountNumber
        self.firstName = fname
        self.lastName = lname
        self.balance = balance

    def getAccNo(self):
        return self.accountNumber

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getBalance(self):
        return self.balance

    def Deposit(self, amount):
        self.balance += amount

    def Withdraw(self, amount):
        if self.balance - amount < 500:
            raise InsufficientFunds()
        self.balance -= amount

    @staticmethod
    def setLastAccountNumber(accountNumber):
        Account.NextAccountNumber = accountNumber

    @staticmethod
    def getLastAccountNumber():
        return Account.NextAccountNumber

    def __str__(self):
        return f"First Name: {self.firstName}\nLast Name: {self.lastName}\nAccount Number: {self.accountNumber}\nBalance: {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}
        try:
            with open("Bank.data", "r") as file:
                for line in file:
                    accountNumber, firstName, lastName, balance = line.strip().split(",")
                    self.accounts[int(accountNumber)] = Account(firstName, lastName, float(balance))
                Account.setLastAccountNumber(int(accountNumber))
        except FileNotFoundError:
            pass

    def OpenAccount(self, fname, lname, balance):
        account = Account(fname, lname, balance)
        self.accounts[account.getAccNo()] = account
        with open("Bank.data", "w") as file:
            for account in self.accounts.values():
                file.write(f"{account.getAccNo()},{account.getFirstName()},{account.getLastName()},{account.getBalance()}\n")
        return account

    def BalanceEnquiry(self, accountNumber):
        return self.accounts.get(accountNumber)

    def Deposit(self, accountNumber, amount):
        account = self.accounts.get(accountNumber)
        if account:
            account.Deposit(amount)
            with open("Bank.data", "w") as file:
                for account in self.accounts.values():
                    file.write(f"{account.getAccNo()},{account.getFirstName()},{account.getLastName()},{account.getBalance()}\n")
            return account
        return None

    def Withdraw(self, accountNumber, amount):
        account = self.accounts.get(accountNumber)
        if account:
            try:
                account.Withdraw(amount)
                with open("Bank.data", "w") as file:
                    for account in self.accounts.values():
                        file.write(f"{account.getAccNo()},{account.getFirstName()},{account.getLastName()},{account.getBalance()}\n")
                return account
            except InsufficientFunds:
                print("Insufficient funds!")
                return None
        return None

    def CloseAccount(self, accountNumber):
        if accountNumber in self.accounts:
            del self.accounts[accountNumber]
            with open("Bank.data", "w") as file:
                for account in self.accounts.values():
                    file.write(f"{account.getAccNo()},{account.getFirstName()},{account.getLastName()},{account.getBalance()}\n")
            print("Account deleted!")

    def ShowAllAccounts(self):
        for account in self.accounts.values():
            print(account)

def main():
    bank = Bank()
    while True:
        print("Banking System")
        print("1. Open an Account")
        print("2. Balance Enquiry")
        print("3. Deposit")
        print("4. Withdrawal")
        print("5. Close an Account")
        print("6. Show All Accounts")
        print("7. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            balance = float(input("Enter initial Balance: "))
            account = bank.OpenAccount(fname, lname, balance)
            print("Congratulations! Account is created.")
            print(account)
        elif choice == 2:
            accountNumber = int(input("Enter Account Number: "))
            account = bank.BalanceEnquiry(accountNumber)
            if account:
                print("Your Account Details:")
                print(account)
            else:
                print("Account not found!")
        elif choice == 3:
            accountNumber = int(input("Enter Account Number: "))
            amount = float(input("Enter Balance: "))
            account = bank.Deposit(accountNumber, amount)
            if account:
                print("Amount is deposited.")
                print(account)
            else:
                print("Account not found!")
        elif choice == 4:
            accountNumber = int(input("Enter Account Number: "))
            amount = float(input("Enter Balance: "))
            account = bank.Withdraw(accountNumber, amount)
            if account:
                print("Amount withdrawn.")
                print(account)
            else:
                print("Account not found!")
        elif choice == 5:
            accountNumber = int(input("Enter Account Number: "))
            bank.CloseAccount(accountNumber)
            print("Account closed.")
        elif choice == 6:
            bank.ShowAllAccounts()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
