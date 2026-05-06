from datetime import datetime  # importing time module to print time of transaction
import random  # importing random module to generate a random account number for customer
from abc import ABC, abstractmethod   # importing abstract base class module


class Account(ABC):  # abstract class

    def init(self, balance=0):  # initializing instance variable balance
        # balance initially sets to zero
        self.balance = balance
        self.timestamp = datetime.now()

    def Deposit(self):   # a method to deposit money in account
        pass  # method will be override by subclasses

    def Withdraw(self):   # a method to withdraw money in account
        pass  # method will be override by subclasses

    @abstractmethod
    def BalanceEnquiry(self):   # making the method abstract to enforce its implementation in all subclasses
        pass


class SavingAccount(Account):
    TransactionHistory = []  # stores all the transactions made by saving account

    def __init__(self, interest_rate=0.1):
        self.interest_rate = interest_rate
        super().__init__()
        self.timestamp = datetime.now()  #prints the current time

    def Deposit(self):
        self.acc = input('Enter account no. :')
        self.Saving = []  # initialize a list for savingAccountDetails file which  store all data of that file.
        f = open("SavingAccountDetails.txt")
        readSavingFile = f.readlines()
        # it read  savingAccountDetails file and convert all data into list seperated by spaces in the form of strings
        f.close()

        for i in readSavingFile:  # it points the one item of the readSavingFile list
            i = i.strip('\n')  # to remove all the \n from the readSavingFile list
            self.Saving.append(eval(i))  # it eval the item then append into a list calles Saving

        for i in self.Saving:  # it points to item of Saving list
            for j in i:  # Now it points to one item of Saving list
                if self.acc == j:
                    self.deposit = float(input('How much amount you want to deposit in your account? '))
                    self.deposit += self.deposit * self.interest_rate
                    # it adds interest rate in your account on the basis of how much amount you deposited
                    i[-2] += self.deposit
                    # actually i[-2] is the total balance of the customer so it add the deposited amount
                    timestamp = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")  # calculate current time
                    print(f"Amount:{self.deposit}\nTime:{timestamp}")
                    print(f'Deposited successfully an amount of {self.deposit} Rs. on your account.')
                    self.TransactionHistory.extend([self.acc, self.deposit, "Deposited",timestamp])
                    # it adds your transaction history into TransactionHistory list

        f1 = open("TransactionHistory.txt", "a")
        f1.write(str(SavingAccount.TransactionHistory) + "\n")
        # now it writes the transaction history of Saving account into TransactionHistory.txt file
        f1.close()

        f = open("SavingAccountDetails.txt", 'w')
        st = ''
        for i in self.Saving:
            st += str(i) + '\n'  # write Saving list into the SavingAccountDetails.txt file in the form of list
        f.write(st)
        f.close()

    def Withdraw(self):
        self.Saving = []  # initialize a list for savingAccountDetails file which  store all data of that file.
        self.acc = input('Enter account no. : ')

        f = open('SavingAccountDetails.txt')
        readSavingFile = f.readlines()
        # it read  savingAccountDetails file and convert all data into list seperated by spaces in the form of strings
        for i in readSavingFile:  # it points the one item of the readSavingFile list
            i = i.strip('\n')  # to remove all the \n from the readSavingFile list
            self.Saving.append(eval(i))  # it eval the item then append into a list called Saving
        f.close()
        for i in self.Saving:  # it points to item of Saving list
            for j in i:  # now it point to one item of Saving list
                if self.acc == j:
                    withdrawal = float(input('how much amount you want to withdraw from your account?'))
                    if i[-2] >= withdrawal and (i[
                                                   -2] - withdrawal) >= 500:  # it checks whether our total balance is >= our withdrawl and remaining balance after subtacting withdrawl from balance is >500 bcz min balance limit is 500
                        i[-2] -= withdrawal  # now it subtract withdrawl amount from total balance
                        timestamp = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")  # calculate current time
                        print(f"Amount:{withdrawal}\nTime:{timestamp}")
                        print(f'withdrew successfully an amount of {withdrawal} Rs. on your account.')
                        self.TransactionHistory.extend([self.acc, withdrawal, "withdrawn",timestamp])
                        # append our transaction history into the TransactionHistory list
                    else:
                        print('sorry you dont have enough amount for withdraw you are overdrawn.')

        f1 = open("TransactionHistory.txt", "a")
        f1.write(str(SavingAccount.TransactionHistory) + "\n")
        # append our transaction history into the TransactionHistory file
        f1.close()

        f = open("SavingAccountDetails.txt", 'w')
        st = ''
        for i in self.Saving:
            st += str(i) + '\n'  # writes Saving list into the SavingAccountDetails.txt file in the form of list
        f.write(st)
        f.close()

    def customer_saving_account_report(self):
        self.c_account_ = input("Enter your account number to see your account details: ")
        f=open("SavingAccountDetails.txt")
        for i in f:
            if self.c_account_ in i:
               print(str(i))
               return
        print("""There is no saving account with this account number :(
              please check and try again..""")
        f.close()


    def BalanceEnquiry(self):
        """this method prints the current balance of our account"""
        self.Saving = []  # initialize a list for savingAccountDetails file which  store all data of that file.
        self.acc = input('Enter your account no.')
        f = open("SavingAccountDetails.txt")
        readSavingFile = f.readlines()
        # it read  savingAccountDetails file and convert all data into list seperated by spaces in the form of strings
        for i in readSavingFile:
            # it points the one item of the readSavingFile lis
            i = i.strip('\n')
            # to remove all the \n from the readSavingFile list
            self.Saving.append(eval(i))  # it eval the item then append into a list called Saving

        for a in self.Saving:  # it points to item of Saving list
            for b in a:  # now it points to one item of Saving list
                if self.acc == b:
                    print('the current balance in your saving account is Rs', a[-2])
                    return

        print("Sorry, we couldn't find your account. Please check your account number and try again.")


class Loan:
    def __init__(self):
        self.l = LoanAccount()  #composition is done
        # loan is the container class and loan account is the content class
        self.timestamp = datetime.now()

    def loan(self):

        # setting a condition that whoever apply for loan must have either saving or checking account
        print("""It is informed that you are eligible to apply for loan if and only if:
         * you have either saving or checking account in our bank""")
        self.reference_account = input( """You are taking loan with which account's reference checking or saving?
         press 'S' if saving or 'C' if checking...""").lower()
        self.a = False
        if self.reference_account == "c":
            self.account = input("Enter your checking account number to process: ")
            print("Verifying....")
            f = open("CheckingAccountDetails.txt")  #verifying if the user has checking account
            for i in f:
                if self.account in i:
                    print("Verified!")
                    self.a = True
                    break
            ## print("Sorry! You do not hava a Checking account ultimately you can not open loan account.")

        elif self.reference_account == "s":
            self.account = input("Enter your saving account number to process: ")
            print("Verifying....")
            f = open("SavingAccountDetails.txt")  #verifying if the user has saving account
            for i in f:
                if self.account in i:
                    print("Verified!")
                    self.a = True
                    break
            ## print("Sorry!You do not hava a Saving account ultimately you can not open loan account.")
        else:
            print("press 'S' or 'C'...")
        if self.a == True:
            _ = int(input("""******Welcome******
                    1. Take loan
                    2. Pay Loan
            press '1' or '2'..."""))
            if _ == 1:
                self.application_for_loan()
            if _ == 2:
                acc = input("Enter Your Loan Account no. : ")
                usern = input('Enter your username of loan account: ')
                loaN = []
                f = open("LoanAccountDetails.txt")  #verifying if the user has entered correct account number
                read_ = f.readlines()
                for u in read_:
                    u = u.strip('\n')
                    loaN.append(eval(u))
                for a in loaN:
                    if acc in a:
                        self.l.pay_loan(acc, loaN, usern)
                        break
                ## print("Sorry you have no loan account.")

    def application_for_loan(self):
        while True:
            apply = input("""If you apply for loan, it is advisable to read the terms and conditions carefully
            press "Y" to read the terms and conditions""").lower()
            if apply == "y":  # describing the terms and conditions for loan
                agree = input("""Terms and Conditions:
                    1.The Bank will charge a certain rate of interest on the loan which varies with the loan amount.
                    2.You can take 500 as minimum loan amount and 100000 as maximum.
                    3.You must decide the repayment period firstly.
                    4.The repayment period must be within 12 months.
                    5.The installment amount will be based on your repayment period.
               press "Y" if you agree the above terms and conditions
               or press "E" to exit!!!""").lower()
                if agree == "e":
                    break

                elif agree == "y":   # taking necessary information if the user agree
                    user = input('Enter your user name for loan account: ')
                    amount = float(input("How much amount you want to take as loan ???"))
                    print(""" According to our terms and conditions:
                    * The installment amount will be based on your repayment period.""")
                    duration = float(input("""In how many installments you will pay back the loan?
                   Enter your response in months: 
                   i.e. 12 if 1 year. """))

                    if amount < 500.0 or amount > 100000.0:  #condition for loan amount
                        # bank don't offer loan amount less than 500 or greater than one lac
                        print("Sorry we do not offer loan of the amount.")
                    else:
                        print("""Congratulations! Your loan has been guaranteed :)""")  #loan guaranteed
                        timestamp = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
                        print(f"Amount:{amount}\nTime:{timestamp}")
                        loan_details = [self.account, amount, duration, user]   #saving details of loan account

                        a = input("""Press Y if you want to get details about the payment of loan: 
                        press "E" to exit : """).upper()
                        if a == "Y":
                            # calls a method to print details of loan account
                            self.l.get_payment_details(amount, duration, loan_details, user)
                            break
                        else:
                            break
                else:
                    print("You are not eligible for loan under terms and conditions")


class LoanAccount(Account):
    def __init__(self, loan_amount=0, interest_rate=0, loan_duration=12):  # initializing instance variables for class loan account
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_duration = loan_duration
        self.payment_per_installment = 0
        self.loan_details = []
        super().__init__()
        self.timestamp = datetime.now()

        ## print(f"The  loan account has Amount : {self.loan_amount}\nInterest rate:{self.interest_rate}\
        ##   \nLoan duration:{self.loan_duration}")

    def get_payment_details(self, amount, duration, loan_details, user):
        # setting different interest rate on different amount of loan
        if 500.0 <= amount <= 1000.0:
            # no interest on loan of less amount
            print("No interest is applied on your loan")
            self.interest_rate = 0
        elif 1000.0 < amount <= 5000.0:
            print("The interest rate will be 2% of the loan amount per installment")
            self.interest_rate = 0.02 * amount
        elif 5000.0 < amount <= 10000.0:
            print("The interest rate will be 5% of the loan amount per installment")
            self.interest_rate = 0.05 * amount
        elif 10000.0 < amount <= 100000.0:
            print("The interest rate will be 10% of the loan amount per installment")
            self.interest_rate = 0.1 * amount
        total_interest_rate = self.interest_rate * duration
        print("""Your loan account has been created...
        Remember! account number for loan is same as of the account which you used as a reference account.""")
        print(user, "Your net Interest will be", total_interest_rate)
        self.payment_per_installment = round((amount / duration) + self.interest_rate)
        print(user, "Your one time payment is:\nyou will pay",self.payment_per_installment,"Rs. per month")
        loan_details[1] += total_interest_rate
        loan = open("LoanAccountDetails.txt", 'a') #writes loan details to file
        loan.write(str(loan_details) + "\n")
        loan.close()

    def pay_loan(self, acc, loaN, user):  #method to pay loan
        for x in loaN:  #verifying for user loan account
            if acc in x and user in x:
                self.amount = x[1]
                self.repaytime = x[2]
                y = self.amount / self.repaytime
                self.loan_amount = x[1] - y
                x[1] = self.loan_amount
                if self.amount == 0:  #if the user has paid the loan already
                    print("You do not have any loan amount to pay.")
                else:
                    f = open("LoanAccountDetails.txt", "w")
                    st = ''
                    for i in loaN:
                        st += str(i) + '\n'
                    f.write(st)
                    f.close()
                    # writes to file that user has successfully paid the installment
                    print(user, 'you successfully paid installment of your loan')
                    timestamp = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
                    print(f"Amount:{y}\nTime:{timestamp}")

    def BalanceEnquiry(self):  #method that prints the current details of loan account
        self.loanacd = []
        self.acc = input('Enter your  loan account no. : ')
        user = input('Enter your user name:')
        f = open("LoanAccountDetails.txt")
        read = f.readlines()

        for i in read:
            i = i.strip('\n')
            self.loanacd.append(eval(i))
        for a in self.loanacd:
            if self.acc in a and user in a:
                print('the current loan balance in your  account is Rs', a[1])
                return

        print("Sorry, we couldn't find your account. Please check your account number and try again.")


class CheckingAccount(Account):
    TransactionHistory = []  # stores all the transaction made by checking account

    def __init__(self, creditLimit=70000.0):
        self.creditLimit = creditLimit
        super().__init__()
        self.timestamp = datetime.now()  # for printing current datetime

    def interestRate(self):  # calculating interest rate wrt to overdraft fee
        if self.overdraftfee < 1000:
            self.interest_Rate = 0.1 * self.overdraftfee
            return -(self.interest_Rate)
        elif self.overdraftfee < 5000:
            self.interest_Rate = 0.2 * self.overdraftfee
            return -(self.interest_Rate)
        elif self.overdraftfee < 10000:
            self.interest_Rate = 0.3 * self.overdraftfee
            return -(self.interest_Rate)
        else:
            self.interest_Rate = 0.4 * self.overdraftfee
            return -(self.interest_Rate)

    def BalanceEnquiry(self):
        """this method print the current balance of our checking account"""
        self.Checking = []  # initialize a list to store all the details of checking account customer
        self.acc = input('Enter your account no. : ')

        f = open("CheckingAccountDetails.txt")
        # read CheckingAccountDetails file and convert into list in the form of strings separated by commas
        readCheckingFile = f.readlines()

        for i in readCheckingFile:  # it prints one item of the readCheckingFile list
            i = i.strip('\n')  # remove every \n from all the item
            self.Checking.append(
                eval(i))  # eval all the item of the readCheckingFile list and append into Checking list
        for a in self.Checking:  # prints the item to item of the list Checking
            for b in a:  # points item of readCheckingFile
                if a[-2] < 0:  # checks whether balance is in negative range or not
                    print('your balance is in neg range bcz of over drafting')
                if self.acc == b:
                    print('the current balance in your  account is Rs', a[-2])
                    return

        print("Sorry, we couldn't find your account. Please check your account number and try again.")

    def customer_checking_account_report(self):
        self.c_account_ = input("Enter your account number to see your account details: ")
        f=open("CheckingAccountDetails.txt")
        for i in f:
            if self.c_account_ in i:
               print(str(i))
               return
        print("""There is no Checking account with this account number :(
              please check and try again..""")
        f.close()

    def Deposit(self):

        self.Checking = []  # initialize a list to store all the details of checking account customer
        self.acc = input('Enter your checking account no. to process: ')
        self.TransactionHistory.append(self.acc)  # append account num in the TransactionHistory list
        f = open("CheckingAccountDetails.txt")
        # read CheckingAccountDetails file and convert into list in the form of strings separated by commas
        readCheckingFile = f.readlines()
        for i in readCheckingFile:  # it points one item of the readCheckingFile list
            i = i.strip('\n')  # remove every \n from all the item
            self.Checking.append(
                eval(i))  # eval all the item of the readCheckingFile list and append into Checking list
        f.close()
        for i in self.Checking:  # points the item to item of the list Checking
            for j in i:  # points item of readCheckingFile
                if self.acc == j:
                    self.deposit = float(input('How much amount you want to deposit in your account?  '))
                    i[-2] += self.deposit  # add deposited amount into your total balance
                    timestamp = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")  # calculate current time
                    print(f"Amount:{self.deposit}\nTime:{timestamp}")
                    print(f'Deposited successfully an amount of {self.deposit} Rs. on your account.')
                    self.TransactionHistory.extend( [self.deposit, "Deposited", timestamp])
                    # it extends to the transaction history list
                    return
        print("You have entered wrong account number.")
        f1 = open("TransactionHistory.txt", "a")
        f1.write( str(CheckingAccount.TransactionHistory) + "\n")
        # it appends the transection history list into transaction history file
        f1.close()

        f = open("CheckingAccountDetails.txt", 'w')
        st = ''
        for i in self.Checking:  # write the Checking list into CheckingAccountDetails.txt file in the form of str
            st += str(i) + '\n'
        f.write(st)
        f.close()

    def Withdraw(self):
        self.Checking = []  # initialize a list to store all the details of checking account customer
        self.acc = input('enter account no.')

        f = open('CheckingAccountDetails.txt')
        readCheckingFile = f.readlines()
        # read CheckingAccountDetails file and convert into list in the form of strings separated by commas
        for i in readCheckingFile:  # it points one item of the readCheckingFile list
            i = i.strip('\n')  # remove every \n from all the item
            self.Checking.append(
                eval(i))  # eval all the item of the readCheckingFile list and append into Checking list
        f.close()
        for i in self.Checking:  # points the item to item of the list Checking
            for j in i:  # points item of readCheckingFile
                if self.acc == j:
                    withdrawal = float(input('How much amount you want to withdraw from your account? '))
                    if i[-2] + self.creditLimit < withdrawal:
                        # checks whether total balance+credit limit is < withdrawl amount or not
                        print('Sorry!!!,withdrawal amount exceeds credit limit!!!')
                    elif i[-2] > withdrawal:  # checks whether balance is> withdral amount or not
                        i[-2] -= withdrawal  # subtract withdrawl amount from balance
                        timestamp = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")  # calculate current time
                        print(f"Amount:{withdrawal}\nTime:{timestamp}")
                        print(f'withdrew successfully an amount of {withdrawal} Rs.from your account.')
                        self.TransactionHistory.extend(
                            [self.acc, withdrawal, "Withdrawn", timestamp])  ##extend the transection history file
                    else:
                        self.overdraftfee = i[-2] - withdrawal  # calculate overdraftfee
                        print(
                            'that amount is more than you have balance in your account,so overdraft fee has been charged.')
                        i[-2] -= withdrawal
                        i[-2] -= self.interestRate()  # subtract total interest from balance
                        print('Now!! loan of Rs', -(self.overdraftfee),
                              'is added to your loan you have to pay it with the interest rate of Rs',
                              self.interestRate())
                        timestamp = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
                        print(f"Amount:{withdrawal}\nTime:{timestamp}")
        f1 = open("TransactionHistory.txt", "a")
        f1.write(str(CheckingAccount.TransactionHistory) + "\n")
        # append  TransactionHistory list into TransactionHistory.txt
        f1.close()

        f = open("CheckingAccountDetails.txt", 'w')
        st = ''
        for i in self.Checking:
            st += str(i) + '\n'  # write the Checking list into CheckingAccountDetails.txt file in the form of string
        f.write(st)
        f.close()


class Customer:
    login_status = ""  #keeps track whether the customer login to saving or checking account

    def login(self):
        self.login_status = input("""which account you want to login?
        1. Checking Account
        2. Saving Account""")
        if self.login_status == "1":
            Customer.login_status = "1"
            print("log in to checking account...")
            self.email_ = input("Enter your email_address: ")
            self.pass_ = input("Enter your password of checking account:  ")

            f = open("CheckingAccountDetails.txt")  #verifying if the user is registered in checking account or not
            for i in f:
                if self.email_ in i:
                    if self.pass_ in i:
                        print("<<<<<<<Welcome>>>>>>")
                        services()
                        return
            print("Wrong email or account no entered")
            f.close()

        elif self.login_status == "2":
            Customer.login_status = "2"
            print("log in to saving account...")
            self.email_ = input("Enter your email: ")
            self.pass_ = input("Enter your password of saving account:  ")

            f = open("SavingAccountDetails.txt")  #verifying if the user is registered in saving account or not
            for i in f:
                if self.email_ in i:
                    if self.pass_ in i:
                        print("<<<<<<<Welcome>>>>>>")
                        services()
                        return
            print("Wrong email or account no entered")
            f.close()

    def signup(self):
        """A method which creates bank account and stores the user info"""
        customer_details = []   # list that saves all the information of user in files
        print("Signing up...")
        while True:
            #keeping track which type of account customer has opened
            signup_status = input("""Which type of account you want to create? 
            1.Checking Account
            2.Saving Account
            press 1 or 2 """)
            # taking information from user
            self.f_name = input("Enter your First Name: ").title()
            self.l_name = input("Enter your Last Name: ").title()
            self.name = self.f_name + " " + self.l_name
            customer_details.append(self.name)
            while True:
                self.email_address = input("Enter your Email Address: ")
                if not (self.email_address.endswith("@gmail.com")):
                    print("kindly enter valid email address")

                else:
                    customer_details.append(self.email_address)
                    break
            while True:
                self.contact_no = input("Enter your contact_no: ")
                if not (len(self.contact_no) == 11) or not (self.contact_no.isdigit()):
                    print("""Invalid length!!!
    enter only digits without spaces!!""")

                else:
                    customer_details.append(self.contact_no)
                    break
            while True:
                self.password = input(
                    "Set a password for your account:\nlength of password must be 6 containing at least 1 special character\n")

                if not (len(self.password) == 6) or not (self.password.isascii()):
                    print("Invalid password")

                else:
                    # customer's account has been created
                    print(f"{self.name} you have successfully logged in\nYour account has been created...")
                    customer_details.append(self.password)
                    print()
                    break

            while True:
                # user must deposit minimum 500 Rs. to open new account
                print("To open a new account, you must have to deposit minimum 500 Rs.")
                self.balance = float(input('How much money you want to deposit ? '))
                if self.balance < 500.0:
                    print('you should have minimum 500 Rs.')
                else:
                    customer_details.append(self.balance)
                    print(self.name + "!", self.balance, "Rs. successfully deposited to your account.")
                    print()
                    # customer's account has been created
                    print(f"{self.name} you have successfully logged in\nYour account has been created...")
                    break

            f = open("accountno.txt", "r")  #opening txt file of account no.
            r = f.read()
            f.close()
            read = r.split()
            #generating random no. as account number for customer
            __ = random.choice(read)
            customer_details.append(__)
            print(self.name + "!", __, "is your account no.")
            print("Remember your account no. & password")
            # deleting the account number once assigned to make sure every customer have distinct account no.
            read.remove(__)

            f = open("accountno.txt", "w")
            for i in read:
                f.write(i + " ")
            f.close()

            if signup_status == "1":
                f = open("CheckingAccountDetails.txt", "a")
                #writes checking account details to file
                f.write(str(customer_details) + "\n")
                f.close()
                break

            elif signup_status == "2":
                f = open("SavingAccountDetails.txt", "a")
                # writes saving account details to file
                f.write(str(customer_details) + "\n")
                f.close()
                break

            else:
                print("Press 1 or 2...")

class Issues:
    issue_count = 0

    def report_issue(self):
        try:
            issues = []
            _customer = input("Enter your email address: ")
            assert _customer.endswith("@gmail.com")
            print("""Welcome to Customer Portal!
            Sorry for inconvenience!""")
            issue = input("Write your issue: ")
            issues.extend([_customer, issue]) #saving issues to file
            f = open("Issues.txt", "a")
            f.write(str(issues) + "\n")
            print("your issue has been submitted!\nwe will try to solve your issue as early as possible")
            f.close()
        except:
            print("Enter valid email address!")

        finally:
            print("Thanks for visiting")


class Admin:
    admin_code = "iamadmin@OBSP"  #setting the admin code

    def alert_issue(self): #alerts the admin about customer's issue
        f = open("Issues.txt")
        print("Here is the list of issues reported by your customers:\n ")
        for i in f:
            print(f.read())
        f.close()

    def customer_database(self):
        """a method which prints the database of customers having checking account,
        loan account and saving account"""
        f1 = open("CheckingAccountDetails.txt")
        print("Database of customers having 'Checking Account':\n")
        checking_account_details = []
        readCheckingAccountDetails = f1.readlines()
        for i in readCheckingAccountDetails:
            i = i.strip('\n')
            checking_account_details.append(eval(i))
        f1.close()
        for a in checking_account_details:
            for b in a:
                if a[-1] == b:
                    print(str(b) + '.', end='')
                else:
                    print(str(b) + ', ', end='')

            print()
        f2 = open("SavingAccountDetails.txt")
        print("\nDatabase of customers having 'Saving Account':\n")
        saving_account_details = []
        readSavingAccountDetails = f2.readlines()
        for x in readSavingAccountDetails:
            x = x.strip('\n')
            saving_account_details.append(eval(x))
        f2.close()
        for y in saving_account_details:
            for z in y:
                if y[-1] == z:
                    print(str(z) + '.', end='')
                else:
                    print(str(z) + ', ', end='')

            print()
        f3 = open("LoanAccountDetails.txt")
        print("\nDatabase of customers having 'Loan Account':\n")
        loan_account_details = []
        readLoanAccountDetails = f3.readlines()
        for j in readLoanAccountDetails:
            j = j.strip('\n')
            loan_account_details.append(eval(j))
        f3.close()
        for m in loan_account_details:
            for n in m:
                if m[-1] == n:
                    print(str(n) + '.', end='')
                else:
                    print(str(n) + ', ', end='')

            print()


class PayBill:
    """A method which allows the user to pay bills"""
    def __init__(self, check, save):
        self.check = check
        self.save = save
        self.timestamp = datetime.now()

    def pay_process(self):
        try:
            response = input("""using this service, you can pay your:
                 1.Electricity Bill
                 2.Water Bill
                 3.Internet Bill
            Enter the name of bill 
             e.g:'electricity' for electricity bill\n             'water' for water bill\n             'internet' for internet bill.""").upper()
            assert response == 'ELECTRICITY' or response == 'WATER' or response == 'INTERNET'
            print('which account you have?checking account or saving account\nif you have both then which account you use to pay bill?')
            ques = input("press 'c' if you want to pay electricity bill from checking or 's' for saving account: ").lower()
            if ques == 'c':
                self.acc = input('Enter your checking account no. : ')
                a = open('CheckingAccountDetails.txt')
                self.Checking = []
                readChecking = a.readlines()
                for i in readChecking:
                    i = i.strip('\n')
                    self.Checking.append(eval(i))
                for i in self.Checking:
                    for j in i:
                        if self.acc == j:
                            bill = float(input('Enter your  bill amount:'))
                            if i[-2] + self.check.creditLimit < bill:
                                print(f'Sorry!!!,{response} bill amount exceeds credit limit!!!')
                            elif i[-2] > bill:
                                i[-2] -= bill
                                timestamp = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
                                print(f"Amount:{bill}\nTime:{timestamp}")
                                print(f'successfulley paid {response} bill of rs{bill} from your checking account.')
                            else:
                                self.check.overdraftfee = i[-2] - bill
                                print(f'that {response} bill amount is more than you have balance in your account,so overdraft fee has been charged.')
                                i[-2] -= bill
                                i[-2] -= self.check.interestRate()
                                print('Now!! loan of Rs', -(self.check.overdraftfee),
                                      'is added to your loan you have to pay it with the interest rate of Rs',
                                      self.check.interestRate())
                                timestamp = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
                                print(f"Amount:{bill}\nTime:{timestamp}")
                a.close()
                f = open("CheckingAccountDetails.txt", 'w')
                st = ''
                for i in self.Checking:
                    st += str(i) + '\n'
                f.write(st)
                f.close()
            elif ques == 's':
                self.Saving = []
                self.acc = input('enter saving account no.')
                f = open('SavingAccountDetails.txt')
                readSaving = f.readlines()
                for i in readSaving:
                    i = i.strip('\n')
                    self.Saving.append(eval(i))
                for i in self.Saving:
                    for j in i:
                        if self.acc == j:
                            bill = float(input('enter your  bill amount:'))
                            if i[-2] >= bill and (i[-2] - bill) >= 500:
                                i[-2] -= bill
                                timestamp = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
                                print(f"Amount:{bill}\nTime:{timestamp}")
                                print(f'{response} bill of RS {bill} successfully paid from your saving account .')

                            else:
                                print(
                                    f'sorry you dont have enough amount to pay {response} bill from your saving account.')
                f.close()
                f = open("SavingAccountDetails.txt", 'w')
                st = ''
                for i in self.Saving:
                    st += str(i) + '\n'
                f.write(st)
                f.close()
            else:
                print("sorry we don't have any other option!")
        except:
            print("Sorry we don't offer more services!!!")


a = "welcome to Online banking system"


def services():
    c = input("""Welcome to our banking app
            We offer following services:
                    1-Manage Account
                    2-Report Issues
                    3-Pay Bill
                    4-Apply for loan
            press \'1\' or \'2\'....""")
    c_ = Customer()
    if c == "1":
        while True:
            b_ = input("""Mode of transaction:
                1.Withdraw
                2.Deposit
                3.Balance Enquiry
                4.Account Details
                press 1. 2. 3. 0r 4.
                press 'E' to exit""")
            if Customer.login_status == "1":
                ch = CheckingAccount()
                if b_ == "1":
                    ch.Withdraw()

                elif b_ == "2":
                    ch.Deposit()

                elif b_ == "3":
                    ch.BalanceEnquiry()

                elif b_ == "4":
                     ch.customer_checking_account_report()

                elif b_ == "e" or b_ == "E":
                    break
                else:
                    print("press 1,2 or 3...")
            elif Customer.login_status == "2":
                s = SavingAccount()
                if b_ == "1":
                    s.Withdraw()

                elif b_ == "2":
                    s.Deposit()

                elif b_ == "3":
                    s.BalanceEnquiry()

                elif b_ == "4":
                    s.customer_saving_account_report()
                elif b_ == "e" or b_ == "E":
                    break

                else:
                    print("press 1,2 or 3...")

    elif c == "2":
        i = Issues()
        i.report_issue()


    elif c == "3":
        check = CheckingAccount()
        save = SavingAccount()
        p = PayBill(check, save)
        p.pay_process()


    elif c == "4":
        l = Loan()
        l.loan()

    ## if True: #2 yahan pr search kry agr pehle se account se associated koi loan he to pay loan ka option de.

    else:
        print("Invalid input")


a = a.center(150)
print(a.title())
try:
    verify = input("""                    1. login as User
                    2. login as administrator
                    press 1 or 2:""")
    if verify == "1":
        a = input("""press \'1\' to login if you already have account or
press \'2\' for signup to create new account
                   1.login
                   2.Signup""")
        if a == "1":
            c = Customer()
            c.login()

        if a == "2":
            c = Customer()
            c.signup()

    elif verify == "2":
        a = Admin()
        _ = input("Enter your admin Code to process: ")
        if _ == Admin.admin_code:
            print("Welcome!!! ")
            b = input("""1.Customer Database
2.Issues
3.Transaction History
press \'1\' or \'2\' or '3'...: """)

            if b == "1":
                print("""Here is the database of your Customers
showing their
*- Name
*-email_address
*-Contact number
*-Password 
*-Account number 
*-Balance\n""")
                a.customer_database()

            elif b == "2":
                a.alert_issue()

            elif b == "3":
                print("Here is the history of transactions made by your customers:")
                f = open("TransactionHistory.txt")
                print(f.read())
                f.close()
            else:
                print("Enter \'1\' or \'2\' only...")

        else:
            print("Wrong admin code entered!")
    else:
        print("Enter \'1\' or \'2\' only...")

except ValueError:
    print("Error! Invalid input")
