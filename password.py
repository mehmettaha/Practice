import random
import string
def passgen():
    psw = []
    op_list = []
    for i in string.ascii_letters:
        op_list.append(i)
    for i in ["?","!",",","\"","*","?","=","-","_","%","#"]:
        op_list.append(i)
    for i in range(0,9):
        op_list.append(str(i))
    pass_length = random.randint(6,10)
    for i in range(pass_length):
        psw.append(random.choice(op_list))
    return "".join(psw)

print(passgen())


   



