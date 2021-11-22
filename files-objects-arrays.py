# prompt user for input
name = input("enter a file name : ")
# if no filename entered then open 'clown.txt' file in root folder
if len(name) < 1:
    name = 'clown.txt'
# open is keyword in python to open a file. we already asked user for this in previous command
fileOpen = open(name)
# create a new empty key:value object called wordList
wordList = dict()
# read each in line in the file we opened
for line in fileOpen:
    # create a new array for every line with each word in it .split() returns an array and .strip removes whitespace
    words = line.strip().split()
    # print the newly created array for each line
    print("the array :\n ",words)

    # if there is an empty line with no words then skip and contiue to next line
    if len(words) < 1:
        continue
    # iterate each word in words array and add it wordList object created at start
    for word in words:
        # and the the current word as key to wordList object and value should increment by 1
        # the .get(value,check) returns zero if value doesnt exist and adds 1
        wordList[word] = wordList.get(word,0) + 1
# print the the object key values with words and occurrences
print("the object :\n ",wordList.items())
# create a new array called newList
newList = list()
# interate through the key and value in wordlist one bye one as tuples
for k,v in wordList.items():
    # creates a temporary with switched key values
    newTup = (v,k)
    # adds this tuple to the newList array
    newList.append(newTup)
# print the the array of tuples unsorted
print("the new object unsorted: \n",newList)
# sort the array of objects in ascending order and print it
newList = sorted(newList)
print("the new object sorted : \n",newList)
# reverse the order of sort and print it
newList = sorted(newList, reverse=True)
print("the new object sorted and reversed: \n",newList)
# iterate and print each object key and value but reverse order
for v,k in newList:
    print(k,v)
