import Levenshtein

f = open('long_read_4.txt', "r")
longReads = f.readlines()
i = 0
for x in longReads: 
    longReads[i] = x[:-2]
    i+=1
    
q = open('short_read_4.txt', "r")
shortReads = q.readlines()
i = 0
for x in shortReads: 
    shortReads[i] = x[:-1]
    i+=1


buckets = []
bucketsKeys = []
buckDict = {}
with open('buckets-4.txt', 'r') as input_file:
    for line in input_file:
        buckets.append(line.strip())  




print(len(bucketsKeys))

for i in buckets:
    temp = i.split(':')
    bucketsKeys.append(temp[0].strip())


for i in buckets:
    temp = i.split(':')
    key = temp[0].strip()
    values = temp[1].split()
    
    values = [int(value) for value in values]
    values = [bucketsKeys[value-1] for value in values]
    buckDict[key] = values


indexVal = 'xxxx'
totaled = 0
final = []
mini = 999
i = 0
for lr in longReads:
    for sr in buckDict.keys():
        if(Levenshtein.distance(lr, sr) < 2):
            temp = buckDict.get(sr)
            for q in temp:
                ed = Levenshtein.distance(lr, q,score_cutoff=3)
                if  ed < mini:
                    mini = ed
                    indexVal = q
    final.append(indexVal)
    print(lr, indexVal)

    totaled += mini
    mini = 999
    i+=1

print(i)
print(totaled/i)
