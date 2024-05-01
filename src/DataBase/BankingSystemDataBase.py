import pyodbc

class DatabasenHandel:

    def __init__(self , server, database , username):

        self.SERVER = server     #'LAPTOP-LLIBH4NC'
        self.DATABASE = database # 'BankingSystemProject'
        self.USERNAME = username # 'sina'

        self.cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                            "Server=LAPTOP-LLIBH4NC;"
                            "Database=BankingSystemProject;"
                            "Trusted_Connection=yes;")
    
    def run_select_query(self,query_):
        cursor = self.cnxn.cursor()
        cursor.execute(query_)
        records = cursor.fetchall()

        return records

