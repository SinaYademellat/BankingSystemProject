from abc import ABC, abstractmethod

class person(ABC):

                def __init__(self, first_name:str, family_name:str ,national_code:int, home_town:str):
                        self.first_name = first_name
                        self.family_name = family_name
                        self.national_code = national_code
                        self.home_town = home_town

                @abstractmethod
                def control_panel(self,db):
                        pass