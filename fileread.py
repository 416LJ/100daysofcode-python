fileOpen = open("mbox2.txt")
emails = list()
for line in fileOpen:
    line = line.rstrip()
    words = line.split()

    if (len(words) > 2) and (words[0] == "From"):
        print(words[1])
        emails.append(words[1])
print(emails)