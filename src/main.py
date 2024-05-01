
from Text_Ui.iomap import how_are_you_
from  Security.Authentication import  is_Admin

import sys
sys.path +=['./Roles' ,'./DataBase' ]

from  Roles.Admin import admin_panel
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
                if(is_Admin(path_of_password,claim_password)):
                    admin_panel(my_database_)

                else:
                       print('your password was wrong !')
    
    else:
        print('asas')

