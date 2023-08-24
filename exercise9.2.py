# Pgm to to count the number of repeating words and display the count using Dictionary func

counts={}
lines=input('Enter a line or text:')
words=lines.split()
print('Counting...',words)
for word in words:
  counts[word]=counts.get(word,0)+1
print('Counts:',counts)    
