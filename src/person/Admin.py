import Person


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

        # Task 1
        def Change_Password(self, new_password):
                self.password = new_password



X = admin('sina','yad',1743,'ir','12')
X.show_information()