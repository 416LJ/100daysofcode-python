# theFile = open('mbox2.txt')
# words = theFile.read()
fileName = input("enter the filename : ")
try:
    openedFile = open(fileName)
except:
    print("file cannot be opened : ", fileName)
    print("please enter a valid filename")
    quit()

for line in theFile2:
   print(line.upper().strip())