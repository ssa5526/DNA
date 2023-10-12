import Levenshtein

f = open('long_read_8.txt', "r")
longReads = f.readlines()
i = 0
for x in longReads: 
    longReads[i] = x[:-2]
    i+=1
    
q = open('short_read_8.txt', "r")
shortReads = q.readlines()
i = 0
for x in shortReads: 
    shortReads[i] = x[:-1]
    i+=1


totaled = 0
final = []
mini = 999
i = 0
for lr in longReads:
    for sr in range(len(shortReads)):
        ed = Levenshtein.distance(lr, shortReads[sr],score_cutoff=3)
        if  ed < mini:
            mini = ed
            index = sr
    final.append(shortReads[sr])
    totaled += mini
    mini = 999
    i+=1

print(i)
print(totaled/i)
