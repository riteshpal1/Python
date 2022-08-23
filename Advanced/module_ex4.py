import os
from datetime import datetime


#Create folder
if os.path.exists('test'):
  print('test folder exists')
else:
  os.mkdir('test')
  print('test folder created')

#create a folder path
folder = 'a/b/c/d/e/f'
if os.path.exists('folder'):
  print('path exists')
else:
  os.makedirs('folder')
  print('path created')


# delete a file'

if os.path.exists('faltu.txt'):
  os.unlink('faltu.txt')
  print('faltu.txt deleted')
else:
  print('faltu.txt does not exist')


# delete a folder path
if os.path.exists('Basics/Hello.ipynb'):
  size = os.path.getsize('Basics/Hello.ipynb')
  ctime = os.path.getsize('Basics/Hello.ipynb')
  mtime = os.path.getmtime('Basics/Hello.ipynb')
  isfile = os.path.isfile('Basics/Hello.ipynb')
  isdir = os.path.isdir('Basics/Hello.ipynb')
  print('filename: Basics/Hello.ipynb')
  print('size', size,'bytes')
  print('ctime:', datetime.fromtimestamp(ctime))
  print('mtime:', datetime.fromtimestamp(mtime))
  print('isfile:',isfile)
  print('isdir:', isdir)


# recursive display file tree
print("Recursive display file tree")
for root, dirs, files in os.walk('.'):
  print(f"Folder is {root.upper()}")
  print("Total folders:", len(dirs))
  print("files in this folder are:", files)