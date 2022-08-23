import os
print('Current folder')
print(os.getcwd())
os.listdir()

print("C Drive Content")
os.chdir('C:\\program files')
print(os.getcwd())
print(os.listdir())

address = r'C:\Program files\Python\Python.exe'
if os.path.exists(address):
  print('file exists')
else:
  print('Address is invalid')
  