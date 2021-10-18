import nltk
from nltk.book import *

#Exercise 24
#a
print([w for w in text6 if w.endswith('ise')]) #print a word from text6 if it ends in 'ise' (using a for-loop and an if-condition)
#b
print([w for w in text6 if 'z' in w or 'Z' in w]) #print a word from text6 if it contains 'z' or 'Z' (using a for-loop and an if-condition and separating 'z' and 'Z' because Python treats them as distinct letters)
#c
print([w for w in text6 if 'pt' in w]) #print a word from text6 if it contains 'pt' (using a for-loop and an if-condition)
#d
print([w for w in text6 if w.istitle()]) #print a word from text6 if it starts with a capital letter (using a for-loop and an if-condition)

#Exercise 25
sent = (['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']) #create a list of words 
#a
print([w for w in sent if w.startswith('sh')]) #print a word from sent if it starts with 'sh'
#b
print([w for w in sent if len(w) >4]) #print a word from sent if it has more than 4 characters