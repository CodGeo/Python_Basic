# Pgm to open a file  count the number of repeating words and display the 
# word and count using Dictionary func and double itertion loop

name=input('Enter a file:')
handle=open(name)

counts=dict()
for line in handle:
  words=line.split()
  for word in words:
    counts[word]=counts.get(word,0)+1
    #print('Word:',word,'count:',counts[word])

bigcount=None
bigword=None
for word,count in counts.items():
  if bigcount is None or count>bigcount:
    bigcount=count
    bigword=word
print(bigword,bigcount)    
