# file i/o in python
# f = open('/home/gowtam-dev/Desktop/practice/python/learn-python/demo.txt', 'a')

# print(f.read()) ## file read
# print(f.readline()) ## we can read single line
# print(f.readlines()) ## we can read mutiple line
# f.write("I am not happy \n") # append text and write a  new line

# redFile = open('/home/gowtam-dev/Desktop/practice/python/learn-python/demo.txt', 'r')
# print(redFile.read())

# over writing file
# overR = open('/home/gowtam-dev/Desktop/practice/python/learn-python/file/demo.txt', 'w')

# overR.write("gowtam kumar is very bad boy")
# overRead = open('/home/gowtam-dev/Desktop/practice/python/learn-python/file/demo.txt', 'r')

# print(overRead.read())

# overRead.close()

# createFile = open('/home/gowtam-dev/Desktop/practice/python/learn-python/file/demo.txt'', 'w') ## create a file
# createFile.write("im am learning new file")

# print(createFile)

## delete file 
# import os
# if os.path.exists('/home/gowtam-dev/Desktop/practice/python/learn-python/file/demo.txt'):
#   os.remove('/home/gowtam-dev/Desktop/practice/python/learn-python/file/demo.txt')
# else: 
#   print("This file does not exist")
#   cretefile = open('/home/gowtam-dev/Desktop/practice/python/learn-python/file/demo.txt', 'w')
#   cretefile.write("hello python. i am learn python")

# create folder
import os
# os.makedirs('/home/gowtam-dev/Desktop/practice/python/learn-python/file/new-folder')

## delete folder

if not os.path.exists('/home/gowtam-dev/Desktop/practice/python/learn-python/file/new-folder'):
  print("this folder is not exits")
  os.makedirs('/home/gowtam-dev/Desktop/practice/python/learn-python/file/new-folder') ## create folder
else:
  os.rmdir('/home/gowtam-dev/Desktop/practice/python/learn-python/file/new-folder') ## delete folder


# file inner text loop
# for x in f:
#   print(x)
# f.close() #file close

