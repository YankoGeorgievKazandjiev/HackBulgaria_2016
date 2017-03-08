from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import DB_NAME
from sqlalchemy import *
from module import *
import getpass
import os
from validators import validate_pass, hash_pass
from pass_resend import send_email
from tan_code import *

Session = sessionmaker(bind = engine)
session = Session()


class Bank(BankUser):

    def __init__(self):
        self._user = ""
        self.username = ""
        self.password = ""
        self.choice = 0
        self.message = ""
        self.email = ""


    def home_screen(self):
        os.system('clear')
        print("Chose to:\n 1.Login\n 2.Register\n 3.Forgot password:\n 4.Exit:")
        self.choice = input('>')
        if self.choice == '1':
            self.login()
        elif self.choice == '2':
            self.register()
        elif self.choice == '4':
            self.exit()
        elif self.choice == '3':
            send_email()


    def login(self):
        print('Enter Username: ')
        self.temp_username = input('>')
        print('Enter Password: ')
        self.temp_password= getpass.getpass('>')
        self.password = hash_pass(self.temp_password)
        for user, password in session.query(BankUser.username, BankUser.password).all():
            if self.temp_username in user:
                if password == self.password:
                    self._user = user
                    os.system('clear')
                    print('Wellcome you are logged in as: {}'.format(user))
                    self.create_tan_codes(self.temp_username)
                    return self.user_choice()
                else:
                    os.system('clear')
                    print('Wrong Password!')
                    return self.login()
            else:
                print("No such User!")


    def create_tan_codes(self, temp_username):
        # After user login, program check if he got Tan if not it will be create and send to email
        for user in session.query(BankUser.id).filter(BankUser.username == self.temp_username).all():
            codes = session.query(TanCode.tan_code).filter(TanCode.user_id == user.id).all()

        if len(codes) == 0:
            tan_codes = generate_tan_codes()
            send_tan_codes(self.email, tan_codes)
            save_codes = []
            for tan_code in tan_codes:
                user = session.query(BankUser.id).filter(BankUser.username == self.temp_username)
                save_codes.append(TanCode(user_id = user, tan_code = tan_code))
            session.add_all(save_codes)
            session.commit()


    def user_choice(self):
        old_balance = session.query(BankUser.balance).filter(BankUser.username == self._user).first()[0]
        print('Chose:\n 1.Deposit\n 2.Withdraw\n 3.Exit')
        self.choice = input('>')
        if self.choice == '1':
            os.system('clear')
            print("You chose to deposit:\n")
            amount = input('Enter Amount: ')
            # print("Enter TAN code:\n")
            # self.tan = input('>')
            # self.check_tan_code(self.tan)
            print(self._user)
            new_balance = float(amount) + old_balance
            os.system('clear')
            session.query(BankUser.balance).filter(BankUser.username == self._user).update({'balance' : new_balance})
            print('Deposit Succesfully amount of: {}.\nCurrent balance: {}'.format(amount, new_balance))
            session.commit()
            input("Press Enter to continue...")
            os.system('clear')
            print("Chose what you want to do:\n 1.Deposit and Withdraw\n 3.Exit")
            self.choice = input('>')
            if self.choice == '1':
                os.system('clear')
                self.user_choice()
            elif self.choice == '3':
                self.exit()
            else:
                print("dsadad")
# To do:
    # def check_tan_code(self, tan):
    #
    #     for user in session.query(BankUser.id).filter(BankUser.username == self.temp_username).all():
    #         codes = session.query(TanCode.tan_code).filter(TanCode.user_id == user.id).all()
    #
    #     if str_tan in str_code:
    #         t_code.delete(synchronize_session='fetch')
    #         session.commit()
    #         print("gj")
    #     else:
    #         print("asd")


        if self.choice == '2':
            os.system('clear')
            print("You chose withdraw:")
            amount = input('Enter amount: ')
            if float(amount) <= old_balance:
                new_balance = old_balance - float(amount)
                session.query(BankUser.balance).filter(BankUser.username == self._user).update({'balance' : new_balance})
                os.system('clear')
                print('Withdraw Succesfully amount of: {}.\nCurrent Balace: {}'.format(amount,new_balance))
                session.commit()
                input("Press Enter to continue...")
                os.system('clear')
                print("Chose what you want to do:\n 1.Deposit and Withdraw\n 3.Exit")
                self.choice = input('>')
                if self.choice == '1':
                    os.system('clear')
                    self.user_choice()
                elif self.choice == '3':
                    self.exit()
                else:
                    print("Error!!!!")
            else:
                os.system('clear')
                print("No enough monie!!!")
                self.user_choice()

    def register(self):
        bool_val = True
        os.system('clear')
        print("Wellcome to registration form!\n Enter username:")
        self.username = input('>')
        print("Enter password:")
        while(bool_val):
            self.password = getpass.getpass('>')
            result = validate_pass(self.password)
            os.system('clear')
            if result == False:
                validate_pass(self.password)
            elif result == True:
                bool_val = False
        print("Enter email:")
        self.email = input('>')
        print("Enter message:")
        self.message = input('>')
        session.add_all([
        	BankUser(username = self.username, password = hash_pass(self.password), balance = "300", message = self.message, email = self.email)])
        session.commit()
        os.system('clear')
        print("You are registrated!!!\n Chose what to do:\n 1.Home\n 2.Exit:")
        self.choice = input('>')
        if self.choice == '1':
            self.home_screen()
        elif self.choice == '2':
            self.exit()

    def exit(self):
        session.close()



def main():
    B = Bank()
    B.home_screen()

if __name__ == '__main__':
    main()
