import sys
count1=0
with open(sys.argv[0],'r') as f1:
    for line in f1:
        word1=line.split()
        count1+=len(word1)
print('word count in file =',count1)
