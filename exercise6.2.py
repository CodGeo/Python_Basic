# Pgm to use find and slicing to extract a portion of the string after the colon and 
# convert it into float

str='X-DSPAM-Confidence: 0.8475'
ipos=str.find(':')
piece=str[ipos+2:]
value=float(piece)
print(piece)
