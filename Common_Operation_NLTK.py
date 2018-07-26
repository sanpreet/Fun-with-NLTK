import os
#import the module nltk
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
corpusdir = 'newcorpus2/'
if not os.path.isdir(corpusdir):
    os.mkdir(corpusdir)
# ***************************************************************************************************************************
# Reading the content of the file which is placed inside the directory newcorpus
newcorpus = PlaintextCorpusReader('newcorpus/', '.*')
print("This is the text file inside newcorpus directory:")
print (newcorpus.raw())
# ***************************************************************************************************************************
# Reading the content of the file which is placed inside the directory newcorpus2
newcorpus2 = PlaintextCorpusReader('newcorpus2/', '.*')
print("This is the text file inside newcorpus2 directory:")
print(newcorpus2.raw())
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
######################################################################################################################
file_1_count=newcorpus.words()
print
print("Display of each word of the file inside the directory newcorpus:")
print(file_1_count)
#count the frequency distribution of each word in the text file
fre_count_file_1= nltk.FreqDist(file_1_count)
print
print("Please see the frequency distribution of each word:")
print(fre_count_file_1)
most_common_word = fre_count_file_1.most_common(2)
print
print("See the most two common used words from the file:")
print(most_common_word)

#################################################################################################################
######################################################################################################################
file_2_count=newcorpus2.words()
print
print("Display of each word of the file inside the directory newcorpus2:")
print(file_2_count)
#count the frequency distribution of each word in the text file
fre_count_file_2= nltk.FreqDist(file_2_count)
print
print("Please see the frequency distribution of each word:")
print(fre_count_file_2)
most_common_word = fre_count_file_2.most_common(2)
print
print("See the most two common used words from the file:")
print(most_common_word)
#################################################################################################################
#fetching any word using indexing from any text file which is inside the directory
#Let us start with the File inise the user created corpus newcorpus
last_word = file_1_count[-1]
counting_first_letter = [i[0] for i in file_1_count]
print
print("Please see the last word of the text file under the directory newcorpus")
print(last_word)
##################################################################################################################
#fetching any word using indexing from any text file which is inside the directory
#Let us start with the File inise the user created corpus newcorpus2
last_word = file_2_count[-1]
counting_first_letter_2 = [i[0] for i in file_2_count]
print
print("Please see the last word of the text file under the directory newcorpus2")
print(last_word)
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
print(set(counting_first_letter_2))
diffe= set(counting_first_letter)- set(counting_first_letter_2)
print
print("See the difference")
print(diffe)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%








