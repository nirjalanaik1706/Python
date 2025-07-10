#file positioning
with open('f1.txt','r') as file:
    print(file.read(5))#read first 5 characters
    print(file.tell())#Current position
    file.seek(0) #Move pointer to the start
    print(file.read(15))#read first 5 characters

#writing binary dataa
with open('img.png', 'rb') as file:
    binary_data = file.read()

with open('img_1.png', 'wb') as file_copy:
    file_copy.write(binary_data)


#
import os
if os.path.exists('f2.txt'):
    os.remove('f2.txt')
    print("file deleted")
else:
    print("File does not exists")