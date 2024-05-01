from  Person import person


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


X = customer('sina','yad',1743,'ir',[],[])
X.show_information()