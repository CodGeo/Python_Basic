# Pgm to open a file  count the number of repeating words and display the 
#  common word and count using Dictionary func and sort by values and not keys

fname=input('Enter a file:')
if len(fname)<1:
  fname='clown.txt'

handle=open(fname)

di=dict()
for line in handle:
  line=line.rstrip()
  wds=line.split()
  for word in wds:
    di[word]=di.get(word,0)+1

tmp=list()
for k,v in di.items():
  newt=(v,k)
  tmp.append(newt)

tmp=sorted(tmp,reverse=True)

for v,k in tmp[:5]:
  print(v,k)
