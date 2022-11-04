""" This code is for password validation """
import re
passwd = input("Enter the password: ")
REG_EX_PATTERN = "^(?=.*[a-z])(?=.*[A-Z])(?=.*r'\\d')(?=.*[@$!%?&])[A-Za-zr'\\d'@$!#*?&]{6,16}$"
match_re = re.compile(REG_EX_PATTERN)
res = re.search(match_re,passwd)
if res:
    print("valid password")
else:
    print("Not a valid password")
    