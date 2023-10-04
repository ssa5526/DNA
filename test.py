import Levenshtein

def create_buckets(reads):
    



def create_buckets(shortread):
    buckets = [[shortread[0]]]
    shortread.pop(0)
    ctr = 0
    for i in shortread:
        for x in buckets:
            if Levenshtein.distance(i, x[0]) <= 3:
                x.append(i)
            else:
                buckets.append([i])
        ctr+=1
        if ctr==100:
            exit
    
    return buckets



f = open('long_read.txt', "r")
longReads = f.readlines()
i = 0
for x in longReads: 
    longReads[i] = x[:-2]
    i+=1
    
q = open('short_read.txt', "r")
shortReads = q.readlines()
i = 0
for x in shortReads: 
    shortReads[i] = x[:-1]
    i+=1


buckets = create_buckets(shortReads)
print(buckets)
'''
totaled = 0
final = []
mini = 999
i = 0
for lr in longReads:
    for sr in range(len(shortReads)):
        ed = Levenshtein.distance(lr, shortReads[sr])
        if  ed < mini:
            mini = ed
            index = sr
    final.append(shortReads[sr])
    print(lr, ' ', shortReads[index], ' ', mini)
    totaled += mini
    mini = 999
    i+=1
    print(i)
    print(totaled/i)

'''