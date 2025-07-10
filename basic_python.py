import os

import numpy as np

if os.path.exists('f2.txt'):
    os.remove('f2.txt')
    print("file deleted")
else:
    print("File does not exists")

#complete file handling program
try:
    with open('f1.txt','w') as file:
        file.write("hello sahil\n")
        file.write("How are you : ")

#reading the file
    with open('f1.txt','r') as file:
        print("Reading file content :")
        print(file.read())
#Append to the file
    with open('f1.txt','w') as file:
        file.write('What are you doing')
#read updated content
except Exception as e:
    print(f"an error  occured: {e}")


#Calculating statics
b=np.array([[1,2,3],[4,5,6]])
print(b)
#sum of all elements
print("\nSum: ",np.sum(b))
#mean
print("\nMean: ",np.mean(b))
#Standred deviation
print("\nDeviation: ",np.std(b))
#minimum and maximum
print("\nMinimum: ",np.min(b))
print("\nMaximum: ",np.max(b))
#sum along an axis
print("\nSum along rows: ",np.sum(b,axis=1))
print("\nSum along columns: ",np.sum(b,axis=0))