
import hashlib

def read_Password_file(filename)->str:
    '''
    read only first line.
    Default password : admin
    '''
    try:
        with open(filename) as file:
                result = (file.readline())
                return result
        
    except FileNotFoundError:
         print(f'can`t open << {filename} >> ')

def hash_password(password:str)->str:
     
    salt = 'Sina_yad'
    mix =(password + salt).encode('utf-8')
    hex_hash =hashlib.sha256(mix).hexdigest()

    return hex_hash 

def writing_to_file(filename:str,new_tex:str)->None:
    
    try:
         handel = open(filename,'w')
         handel.write(new_tex)
         handel.close()

    except FileNotFoundError:
        print(f'can`t open << {filename} >> ')

def is_Admin(file_path:str , input_password:str)->bool:
     
    input_password = hash_password(input_password)
    real_password  = read_Password_file(file_path)

    return (input_password == real_password)