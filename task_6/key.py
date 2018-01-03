import os
import sys


def decrypt(file):
    import pyAesCrypt
    print("---------------------------------------------------------------")
    password = "123"
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


walk("/home/dmytrotsko/Desktop/underdefence_practice/task_6")
print("---------------------------------------------------------------")
os.remove(str(sys.argv[0]))