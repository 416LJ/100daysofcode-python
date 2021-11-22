name = input("enter a file name : ")
if len(name) < 1:
    name = 'clown.txt'
fileOpen = open(name)
wordList = dict()
for line in fileOpen:
    words = line.strip().split()
    if len(words) < 1:
        continue
    for word in words:
        wordList[word] = wordList.get(word,0) + 1
print(wordList)

newList = list()
for k,v in wordList.items():
    newTup = (v,k)
    newList.append(newTup)

newList = sorted(newList, reverse=True)

for v,k in newList:
    print(k,v)