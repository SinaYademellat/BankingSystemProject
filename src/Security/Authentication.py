
import hashlib

'''
 we want to read only first line.
 << Passwor >>  : admin
'''
def read_Password_file(filename)->str:

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
    # print(hex_hash)

    # print(type(hex_hash))
    return hex_hash 

