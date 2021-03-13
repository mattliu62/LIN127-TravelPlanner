import glob
import nltk
import collections
import pickle

#ASK USER FOR INPUT, INPUT IS USED TO DETERMINE SOURCE FILE
src = input("Enter your source:\n")
src = src.replace(' ', '')

file_names = glob.glob('/mnt/c/Users/Matthew/Desktop/LIN 127/final/corpus/*.txt')

hit = 0

#CHECK ALL FILES FOR SOURCE FILE
for filename in file_names:
    if src in filename:
        print("You selected " + src + ' as your source.')
        srcFile = open(filename, 'r')
        srcText = srcFile.read()
        srcTokens = nltk.word_tokenize(srcText)
        hit = 1
    else:
        continue

if hit == 0:
    print ("That source is unsupported.")
    exit()
    
#CALCULATE SOURCE FILE FREQUENCY
srcFD = nltk.FreqDist(srcTokens)

#CREATE DICTIONARY, WILL ONLY CONTAIN TOP 3 MATCHES
d = {}

#CHECK ALL NON-SOURCE FILES AND CALCULATE FREQUENCY
for filename2 in file_names:
    if src in filename:
        continue
    else:
        dstFile = open(filename2, 'r')
        dstText = dstFile.read()
        dstTokens = nltk.word_tokenize(dstText)
        dstFD = nltk.FreqDist(dstTokens)
        print(dstFD)


    



