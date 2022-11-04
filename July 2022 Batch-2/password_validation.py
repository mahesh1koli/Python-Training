""" Password Validation """
import re
p = input("Enter password: ")
X = True
while X:
    if (len(p)<6 or len(p)>= 16):
        break
    if not re.search("[a-z]",p):
        break
    if not re.search("[A-Z]",p):
        break
    if not re.search("[$#@]",p):
        break
    if not re.search("[0-9]",p):
        break
    if re.search(r"\s",p):
        break
    print("Valid password")
    X=False
    break

if X:
    print("Not a valid password")
    