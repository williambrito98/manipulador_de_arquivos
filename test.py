import os

files = os.listdir('C:/')
listFiles = []
for file in files:
    tupleFile = (file, file)
    listFiles.append(tupleFile)
print(listFiles[0][0])