from  Person import person
from  Text_Ui.iomap import cutomer_TUI
import os

class customer(person):

        def __init__(self, first_name:str, family_name:str ,national_code:int, home_town:str ,account_number:list, loan_number:list ):
                super(customer, self).__init__(first_name, family_name, national_code, home_town)
                
                self.account_number = account_number
                self.loan_number = loan_number

        # +++++++++++++++++++++++++++++++++++++++++++++++++ << private >> +++++++++++++++++++++++++++++++++++++++++++++++++
        
        def  Requesـnew_account(self,user_request):
                filename = 'Security//Account_Request.txt'
                try: 
                        with open(filename , "a") as f:
                                f.write(user_request)
                except FileNotFoundError:
                        print(f'can`t open << {filename} >> ')

        # ~~~~~~~~~~~~~~~~ << BaseQuery >> ~~~~~~~~~~~~~~~~  

        def BaseQuery_AccountBalance(self)->str:
                qurey = 'SELECT * from Account where account_owner = ' + self.national_code
                return qurey

        #  =================================== << polymorphism >> ===================================

        def control_panel(self,db):
                Check_orders = 0

                while True :
                        customer_order = cutomer_TUI(40)

                        if(customer_order == 1) :
                                requst_is ='user: '+ self.first_name + ','+self.national_code + ' <?> \n'
                                self.Requesـnew_account(requst_is)

                        elif(customer_order == 2) :
                                qurey_str        = self.BaseQuery_AccountBalance()
                                result_query     = db.run_select_query(qurey_str)
                                for r in result_query:
                                        print(r)

                        elif( (customer_order == 3) or (customer_order == 4) ) :

                                # <<  userـaccount_balance  >> 
                                account_number          = input('account_number (8char): ')
                                qurey_str               ='select account_amount FROM Account where account_number = ' + account_number
                                
                                result_query            = db.run_select_query(qurey_str)
                                userـaccount_balance    = float(result_query[0][0])
                                print('cu: ',userـaccount_balance)
                                try:
                                        account_amount = float(input('>> '))
                                except  ValueError:
                                        print("unsuccessful! (input type)")
                                        account_amount =userـaccount_balance
                                        return
                                
                                if(customer_order == 3):
                                                userـaccount_balance -= account_amount
                                else:
                                                userـaccount_balance += account_amount

                                cursor = db.cnxn.cursor()
                                cursor.execute("UPDATE Account SET account_amount = ? WHERE account_owner = ? AND account_number = ?", userـaccount_balance, self.national_code,account_number)
                                db.cnxn.commit()

                        elif( customer_order == 5 ):

                                branch_ID_              = input('branch_ID: ')
                                list_of_all_branch_ID   = db.all_branch_ID()

                                if(branch_ID_ not in list_of_all_branch_ID):
                                        print('we not have this branch')
                                        return 
                                check_list = db.all_branches_where_the_user_has_Loan(self.national_code)
                                max_loan = db.budget_of_this_branch(branch_ID_)

                                # rule one
                                if(int(branch_ID_) in check_list):
                                        print('sry, you did have loan in this branch !')
                                        return
                                # rule two
                                try: 
                                        loan_need = float(input('loan_amount: '))
                                except ValueError:
                                                print("unsuccessful! (input type)")
                                                return
                                if(loan_need  > max_loan):
                                        print('sry, we can not Accept!')
                                        return

                                print('ok')

                        input("\nPress Enter to continue...")
                        os.system("cls" if os.name == "nt" else "clear")
                        Check_orders += 1
                        print('#) ',Check_orders)

