# test
from Security.Authentication import read_Password_file , hash_password

B = read_Password_file('Security//Password.txt')
# print("SINA")
print(B)

hash_password(B)