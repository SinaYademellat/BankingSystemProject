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

    # ----------------------------------------------------------------

    def fetch_customer(self, national_code):
            str_query = "SELECT * FROM customer where national_code = "+ national_code
            result_query = self.run_select_query( str_query )
            return result_query[0]

    def all_user_in_db(self)->list:
        
        result_query = self.run_select_query( " SELECT national_code  from customer ")

        list_of_users = []
        for r in result_query:
            list_of_users.append(str(r.national_code))

        return list_of_users

    def all_branch_ID(self)->list:
        
        result_query = self.run_select_query( " SELECT branch_id  from Branch ")

        list_of_branch_id = []
        for r in result_query:
            list_of_branch_id.append(str(r.branch_id))

        return list_of_branch_id
  
    def budget_of_this_branch(self , branch_id:str)->float:

        
        qurey_str = "SELECT budget from Branch where branch_id = " + branch_id
        result_query = self.run_select_query(qurey_str)
        
        return(result_query[0].budget)

    def all_branches_where_the_user_has_Loan(self, customer_id:str)->list:

        qurey_str = " SELECT branch_id  from Loan where customer_id = " + customer_id
        result_query = self.run_select_query(qurey_str)

        all_branches_has = []
        for r in result_query:
            all_branches_has.append(r.branch_id)
        
        return all_branches_has