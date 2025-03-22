file = open("2025-03-22/newsextract.txt","r")
tally = 0

for line in file:
    wordslist = line.split()
    linelen = len(wordslist)
    tally = tally + linelen
    

print(tally)
file.close()