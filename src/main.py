import sys
sys.path +=['./Roles' ,'./DataBase' ]

from Text_Ui.iomap import how_are_you_ 
from  Security.Authentication import  is_Admin
from  Roles.Admin import admin_panel
from  Roles.Customer import customer_panel
from  DataBase.BankingSystemDataBase import DatabasenHandel


if __name__ == '__main__':

    server ='LAPTOP-LLIBH4NC'
    database = 'BankingSystemProject'
    username = 'sina'
    my_database_ = DatabasenHandel(server,database,username)

    path_of_password = 'Security//Password.txt'

    user_role = how_are_you_(30)

    if user_role == 1:
                claim_password = input('Enter your password :')

                if( is_Admin ( path_of_password, claim_password ) ):
                        admin_panel(my_database_)
                else:
                       print('your password was wrong !')

    else:
        claim_national_code = input('Enter your National Code: ')
        list_of_all_users = my_database_.all_user_in_db()

        if(claim_national_code in list_of_all_users):
                customer_panel(claim_national_code , my_database_)
        else:
                print('your National Code was wrong !')

