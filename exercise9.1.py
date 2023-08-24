# Pgm to to count the number of repeating names and display the count using Dictionary func

counts=dict()
names=['krish','Roshan','Haafis','krish','Roshan']
for name in names:
  counts[name]=counts.get(name,0)+1
print(counts)
