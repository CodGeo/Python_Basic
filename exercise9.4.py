# Pgm to open a file  count the number of repeating words and display the 
#  common word and count using Dictionary func and double itertion loop

fname=input('Enter a file:')
# so that entering 'Enter key' defaulted to clown.txt
if len(fname)<1:     
  fname='clown.txt'

# Assigning handle name of the file to open
handle=open(fname)

#define dictionary
di=dict()
for line in handle:
  #removing whitespaces or \n or empty spaces from each line
  line=line.rstrip()
  #print('Line:',line)
  #stripping out each word from the line, stripped based on the space between the words
  wds=line.split()
  #print('Words:', wds)
  for word in wds:
    
    # idiom to create, retrieve & update counter
    # the code essentially checks if the word is already a key in the dictionary. 
    #If it is, it increments the count of that word; 
    #if it's not, it adds the word to the dictionary with a count of 1.
    
    di[word]=di.get(word,0)+1

#print(di)

#to find the most common word

largest=-1
theword=None
#key,value k,v
for k,v in di.items():
  if v>largest:
    largest=v
    theword=k
  
print(theword,largest)
