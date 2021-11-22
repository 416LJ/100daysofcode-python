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
biggest = -1
bigWord = None
for k,v in wordList.items():
    if v > biggest:
        biggest = v
        bigWord = k
    print(v,k)
print("done : ", bigWord, biggest)

