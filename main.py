authorDict = dict()
titleDict = dict()
totalRunTime = 0
counter = 0
file = open("content.txt", "w")
for line in open("data.txt", "r"):
    counter = counter + 1
    contentList = line.strip().split("|")
    totalRunTime += float(contentList[0].strip())
    title = contentList[1].strip()
    author = contentList[2].strip()
    if title[0].upper() not in titleDict:
        titleDict[title[0].upper()] = set()
        titleDict[title[0].upper()].add(title.title())
    else:
        titleDict[title[0].upper()].add(title.title())
    if author[0].upper() not in authorDict:
        authorDict[author[0].upper()] = set()
        authorDict[author[0].upper()].add(author.title())
    else:
        authorDict[author[0].upper()].add(author.title())


file.write("Titles table of contents:\n")
for titleLetter in sorted(titleDict.keys()):
    file.write(titleLetter + ":\n")
    for title in sorted(list(titleDict[titleLetter])):
        file.write(title + "\n")
    file.write('\n')

file.write("Authors table of contents:\n")
for authorLetter in sorted(authorDict.keys()):
    file.write(authorLetter + ":\n")
    for author in sorted(list(authorDict[authorLetter])):
        file.write(author + "\n")
    file.write('\n')

averageRunTime = totalRunTime / counter
aRTMinutes = averageRunTime // 60
aRTSeconds = int(averageRunTime) % 60
file.write("\nAverage length of mp3s in this folder: {} minutes {} seconds".format(int(aRTMinutes), aRTSeconds)) 

file.close()

