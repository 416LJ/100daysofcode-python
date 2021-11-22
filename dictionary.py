bag = {
    "one" : "hello",
    "two" : "world"
}

counts = dict()
names = ["ok", "thanks", "yes", "ok"]
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)

for line in fileOpen:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1
bigCount = 0
bigWord = 0
for word, counts in count.items():
    print(count[word])
    if bigCount is None or counts > bigCount:
        bigWord = word
        bigCount = counts
print(bigCount, bigWord)


