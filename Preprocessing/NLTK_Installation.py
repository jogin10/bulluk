'''
Created on 08.12.2016

@author: Aydin
'''
# Satz- und Wortsegmentierung!
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download()
 
#===============================================================================
# example = "Hallo, wie geht es dir heute? Ich war heute auf Arbeit und bin danach nach Hause gekommen. Das Wetter war ok."
# print(sent_tokenize(example))
# print(word_tokenize(example))
#  
# for i in word_tokenize(example):
#     print (i)
# 
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.corpus.europarl_raw import german
# 
# example_text = "Hallo, wie geht es dir heute? Ich war heute auf Arbeit und bin danach nach Hause gekommen. Das Wetter war ok. Die Eigenschaften von dem Smartphone sind echt schlecht und machen uberhaupt keinen spass."
# stop_words = set(stopwords.words("german"))
# 
# words = word_tokenize(example_text)
# 
# filtered_sentence = []
# 
# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)
# print (filtered_sentence)
#===============================================================================






















