import glob
import nltk
import collections
import pickle
import sklearn
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer

#ASK USER FOR INPUT, INPUT IS USED TO DETERMINE SOURCE FILE
src = input("Enter your source:\n")
src = src.replace(' ', '')

file_names = glob.glob('/mnt/c/Users/Matthew/Desktop/LIN 127/final/corpus/*')
destinations = []
for filename in file_names:
    place = filename.replace('/mnt/c/Users/Matthew/Desktop/LIN 127/final/corpus/', '').replace('-WhatToDo', '').replace('WhatTo', '').replace('.txt', '')
    destinations = destinations + [place]
    destinations = sorted(destinations)
    file_text = open(filename, 'r').read()
    renamed_file = open('/mnt/c/Users/Matthew/Desktop/LIN 127/final/WhatToDo/%s' %  place, 'w') 
    print(file_text, file=renamed_file)
    renamed_file.close
file_names2 = glob.glob('/mnt/c/Users/Matthew/Desktop/LIN 127/final/WhatToDo/*')
hit = 0

#CHECK ALL FILES FOR SOURCE FILE
for filename in file_names:
    if src in filename:
        print("You entered " + src + ' as your source.' + ' File used: ' + filename)
        srcFile = open(filename, 'r')
        srcText = srcFile.read()
        srcTokens = nltk.word_tokenize(srcText)
        hit = 1
    else:
        continue

if hit == 0:
    print ("That source is unsupported. Supported Destinations:\n")
    print(destinations)
    exit()
    
#CALCULATE SOURCE FILE FREQUENCY
srcFD = nltk.FreqDist(srcTokens)

# lines 49-52 from https://stackoverflow.com/questions/8897593/how-to-compute-the-similarity-between-two-text-documents
# a valorous attempt to do this from scratch got close but required more math brains to get right -MM
documents = [open(f,'r').read() for f in sorted(file_names2)]
tfidf = TfidfVectorizer(max_df=.75).fit_transform(documents)
# no need to normalize, since Vectorizer will return normalized tf-idf
pairwise_similarity = tfidf * tfidf.T
#print(tfidf)
similarity_array = pairwise_similarity.A
np.fill_diagonal(similarity_array, np.nan)
open_file_01 = open('/mnt/c/Users/Matthew/Desktop/LIN 127/final/simarray_nltk','w')
print(similarity_array, file=open_file_01)

#CONVERT 2D-ARRAY TO LIST
a2l = similarity_array.tolist()
#print(l)

# FOR INPUT DESTINATION, RETURN CLOSEST MATCH
for place in destinations:
    if src in place:
        src_index = destinations.index(place)
        src_destination = place  

currentPlaceList = a2l[src_index]

#CREATE LIST, WILL ONLY CONTAIN TOP 3 MATCHES
l = []

for i in range(0,3):
    maximum = max(currentPlaceList)
    maxIndex = currentPlaceList.index(maximum)
    l.append(destinations[maxIndex])
    destinations.pop(maxIndex)
    currentPlaceList.pop(maxIndex)

print('Destinations most similar to %s:' % src)
for j in range(0,3):
    print(str(j + 1) + ". " + l[j])

#for i in range (0,3): 
                                                                                                                                                                                               
#    input_doc = documents[src_index]                                                                                                                                                                                               
#    input_idx1 = documents.index(input_doc)                                                                                                                                                                                                                      
#    input_idx1    

 #   src_destination_uc = src_destination.upper()
#    result_idx1 = np.nanargmax(similarity_array[input_idx1])
   # l.append(destinations[result_idx1])   
    
#else:
 #   if (result_idx1 >)

#print('Destinations most similar to %s:' % src_destination_uc)
#print(l)
#print(destinations[result_idx1])                                                                                                                                                                                                                              

#input_idx2[(src_index, result_idx1)] = np.nan
#result_idx2 = np.nanargmax(similarity_array[input_idx2])
#print(result_idx2)
#result_idx3 = np.nanargmax(similarity_array[not (result_idx1 or result_idx2)])
#print(result_idx3)
