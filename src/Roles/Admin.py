
import sys
sys.path.append('..')

import Person
from  Text_Ui.iomap import  admin_TUI
import Security.Authentication as my_Security_headers

class admin(Person.person):
        
        def __init__(self, first_name:str, family_name:str ,national_code:int, home_town:str , password:str):
                super(admin, self).__init__(first_name, family_name, national_code, home_town)
                self.password = password
        
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


#  ======================== << GUI >> =========================

def admin_panel(db):

        server_admin = admin('sina','yad',1743,'ir','*')

        while True : 
                
                admin_order = admin_TUI(40)
                
                if(admin_order == 0):
                        server_admin.show_information()

                elif(admin_order == 1):
                        server_admin.Change_Password('Security//Password.txt')

                elif(admin_order == 2):

                        result_query =  db.run_select_query('SELECT COUNT(*) as number FROM Bank')
                        number_of_banks = result_query[0].number
                        number_of_banks += 1
                        
                        name_of_new_bank = input('Name: ')

                        cursor = db.cnxn.cursor()
                        cursor.execute("INSERT INTO Bank(bank_id , name ) values (?, ?)", number_of_banks, name_of_new_bank)
                        db.cnxn.commit()
                
                elif(admin_order == 3):

                        result_query =  db.run_select_query('SELECT COUNT(*) as number FROM Branch')
                        number_of_Branch = result_query[0].number
                        number_of_Branch += 1

                        name_of_new_Branch = input('Name: ')

                        cursor = db.cnxn.cursor()
                        cursor.execute("  INSERT INTO Branch(branch_id , name ) values (?, ?)", number_of_Branch, name_of_new_Branch)
                        db.cnxn.commit()

                elif(admin_order == 4):
                         
                        branch_id = input('branch_id: ')
                        qurey_str = 'SELECT budget as number FROM Branch where branch_id = ' + branch_id
                        
                        result_query = db.run_select_query(qurey_str)
                        budget = result_query[0].number
                        print(budget)

                elif(admin_order == 5):
                         print ('next time')
                
                elif(admin_order == 6):
                        
                        result_query = db.run_select_query('SELECT *  FROM customer')
                        
                        for r in result_query:    
                                print(' ===================== ')
                                print ('national_code: ' , r.national_code )
                                print ('first_name: ' , r.first_name )
