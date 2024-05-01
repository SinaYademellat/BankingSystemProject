from  Person import person
from  Text_Ui.iomap import cutomer_TUI

class customer(person):

        def __init__(self, first_name:str, family_name:str ,national_code:int, home_town:str ,account_number:list, loan_number:list ):
                super(customer, self).__init__(first_name, family_name, national_code, home_town)
                self.account_number = account_number
                self.loan_number = loan_number
        
        def show_information(self)->None:
                    print(' ------- << customer >> ------ \n'
                          ' name: ' + self.first_name + '\n',
                          'family: ' + self.family_name + '\n',
                          'national_code: ' + str(self.national_code) + '\n',
                          'home_town: ' + self.home_town+'\n', 
                          )
                    
                    if( len(self.account_number)>0 ):
                            print(' << account_list  >> ')
                            for i in range(self.account_number):
                                    print(i)
                    
                    if( len(self.loan_number)>0 ):
                            print(' << loan_number  >> ')
                            for i in range(self.loan_number):
                                    print(i)

        def  New_Account(self, account_number):
                
                filename = 'Security//Account_Request.txt'
                
                try: 
                        with open(filename , "a") as f:
                                requst_is ='user: '+ account_number + ' New Account\n'
                                f.write(requst_is)

                except FileNotFoundError:
                        print(f'can`t open << {filename} >> ')


#  ===========================

def  customer_panel(national_code:str , db):

        test_customer =   customer('sina','yademellat',national_code,'ir',[],[])
        
        while True : 
                customer_order = cutomer_TUI(40)

                if(customer_order == 1) :
                        test_customer.New_Account(national_code)

                elif(customer_order == 2) :

                        qurey_str = 'SELECT * from Account where account_owner = ' + national_code
                        
                        result_query = db.run_select_query(qurey_str)
                        for r in result_query:
                                print(r)

                elif( (customer_order == 3) or (customer_order == 4) ) :

                        account_number = input('account_number (8char): ')
                        account_amount = float(input('account_amount : '))

                        cursor = db.cnxn.cursor()
                        cursor.execute("UPDATE Account SET account_amount = ? WHERE account_owner = ? AND account_number = ?", account_amount, national_code,account_number)
                        db.cnxn.commit()

                elif( customer_order == 5 ):

                        branch_ID_ = input('branch_ID: ')
                        check_list = db.all_branches_where_the_user_has_Loan(national_code)
                        max_loan = db.budget_of_this_branch(branch_ID_)

                        if(branch_ID_.isnumeric()):
                                branch_ID_ = int(branch_ID_)
                        else:
                                print('we not have this branch')

                        # rule one
                        if(branch_ID_ in check_list):
                                print('sry, you did have loan in this branch !')
                                return
                        
                        # rule two
                        loan_need = input('loan_amount: ')
                        if(loan_need  > max_loan):
                                print('sry, we can not Accept!')
                                return
                        
                        print('your requse will check.')

