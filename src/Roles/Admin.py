
import sys
sys.path.append('..')
import os
import Person
from  Text_Ui.iomap import  admin_TUI
import Security.Authentication as my_Security_headers

class admin(Person.person):
        
        def __init__(self, first_name:str, family_name:str ,national_code:int, home_town:str , password:str):
                super(admin, self).__init__(first_name, family_name, national_code, home_town)
                self.password = password
        
        # ~~~~~~~~~~~~~~~~ <<  >> ~~~~~~~~~~~~~~~~  

        def show_information(self)->None:
                        print(' ------- << admin >> ------ \n'
                                ' name: ' + self.first_name + '\n',
                                'family: ' + self.family_name + '\n',
                                'national_code: ' + str(self.national_code) + '\n',
                                'home_town: ' + self.home_town+'\n', 
                                'password: ' + self.password
                                )

        def Change_Password(self, filename:str):
                        new_password = input('password: ')
                        self.password = new_password
                        hex_hash_new_password = my_Security_headers.hash_password(new_password)
                        my_Security_headers.writing_to_file(filename,hex_hash_new_password)

        def Insert_into_Bank(self,database):
                        result_query =  database.run_select_query('SELECT COUNT(*) as number FROM Bank')
                        number_of_banks = result_query[0].number
                        number_of_banks += 1

                        name_of_new_bank = input('Name: ')

                        cursor = database.cnxn.cursor()
                        cursor.execute("INSERT INTO Bank(bank_id , name ) values (?, ?)", number_of_banks, name_of_new_bank)
                        database.cnxn.commit()

        def Insert_into_Branch(self,database):
                        result_query =  database.run_select_query('SELECT COUNT(*) as number FROM Branch')
                        number_of_Branch = result_query[0].number
                        number_of_Branch += 1

                        name_of_new_Branch = input('Name: ')
                        try:
                                budget = float(input('Budget: '))
                        except ValueError:
                                budget = 0

                        cursor = database.cnxn.cursor()
                        cursor.execute("  INSERT INTO Branch(branch_id , name , budget) values (?, ? , ?)", number_of_Branch, name_of_new_Branch , budget)
                        database.cnxn.commit()

        def Branch_budget(self,database):
                        branch_id = input('branch_id: ')
                        qurey_str = 'SELECT budget as number FROM Branch where branch_id = ' + branch_id
                        list_of_all_branch_ID   = database.all_branch_ID()
                        if(branch_id not in list_of_all_branch_ID):
                                        print('we not have this branch')
                                        return 
                        result_query = database.run_select_query(qurey_str)
                        budget = result_query[0].number
                        print(budget)

        def Check_requests(self):
                        filename = 'Security//Account_Request.txt'
                        try: 
                                with open(filename, 'r') as days_file:
                                        days = days_file.read()
                                        print(days)
                        except FileNotFoundError:
                                print(f'can`t open << {filename} >> ')

        def Monitoring(self,database):
                        result_query = database.run_select_query('SELECT *  FROM customer')                 
                        for r in result_query:    
                                print(' ===================== ')
                                print ('national_code: ' , r.national_code )
                                print ('first_name: ' , r.first_name )

        #  =================================== << polymorphism >> ===================================

        def control_panel(self,db):
                Check_orders = 0
                while True : 
                        admin_order = admin_TUI(40)

                        if(admin_order == 0):
                                self.show_information()

                        elif(admin_order == 1):
                                self.Change_Password('Security//Password.txt')

                        elif(admin_order == 2):
                                self.Insert_into_Bank(db)

                        elif(admin_order == 3):
                                self.Insert_into_Branch(db)
                        
                        elif(admin_order == 4):
                                self.Branch_budget(db)

                        elif(admin_order == 5):
                               self.Check_requests()

                        elif(admin_order == 6):
                                self.Monitoring(db)

                        input("\nPress Enter to continue...")
                        os.system("cls" if os.name == "nt" else "clear")
                        Check_orders += 1
                        print('#) ',Check_orders)

