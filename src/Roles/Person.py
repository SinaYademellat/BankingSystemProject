class person:
            def __init__(self, first_name:str, family_name:str ,national_code:int, home_town:str):
                    self.first_name = first_name
                    self.family_name = family_name
                    self.national_code = national_code
                    self.home_town = home_town

            def show_information(self)->None:
                    print(' ------- << person >> ------ \n'
                          ' name: ' + self.first_name + '\n',
                          'family: ' + self.family_name + '\n',
                          'national_code: ' + str(self.national_code) + '\n',
                          'home_town: ' + self.home_town+'\n', 
                          )