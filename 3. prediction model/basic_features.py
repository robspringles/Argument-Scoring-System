
# coding: utf-8

# # Extract basic features for score predicition model 

# In[1]:



# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd


# ## load test data 

# In[2]:

# path = '/Users/apple/Documents/GitHub/Argument-Scoring-System/comment_data/comments.csv'


# # In[3]:

# data = pd.read_csv(path)
# # remove none value 
# new_data = data[np.isfinite(data['mean_evaluation'])]
# X = new_data['comment_text']
# y = new_data['mean_evaluation']


# ## feature preparation 

# * word count 
# * spelling error count 
# * paragraph count 
# * sent count 
# * average sentence length count 
# * punctuation number 
# * average sents in paragragh 
# * average puncts in sents

# In[4]:

import re
from collections import Counter
import language_check
import nltk
import math
import re


# In[5]:

def get_words(text):
    ''' Get all the words in a text 
    :param text: raw text
    :return: all the words in the text
    Example: 
            print (get_words('I amd the .. . /3'))
    '''
    return re.findall(r'\w+', text.lower())


# In[6]:

# Get all the words in en-spelling.txt which contains most words in English dictionary
# words.txt is from https://github.com/dwyl/english-words
# WORDS = Counter(get_words(open('en-spelling.txt').read()))
WORDS = Counter(get_words(open('words.txt').read()))


# In[7]:

def get_spelling_error_number(text):
    '''
    1. Check if it is in the words.txt
    2. Check if it is a number
    Get the number of errors in the text. The spelling error defined here is the words not in en-spelling.txt
    :param text: the raw text
    :return: the number of spelling errors. 
    Example:
            print (get_spelling_error_number("he kk uu in jsas ssssss"))
    '''
    text_words = get_words(text)
    error_numer = 0
    for w in text_words:
        if w not in WORDS:
            if w.isdigit():
                pass
            else:
                error_numer += 1
#                 print (w)
    return float(error_numer)


# In[8]:

# print (X[0])


# In[9]:

def get_word_number(text):
    '''
    Get the number of words (including numbers) in the raw text 
    :param text: the raw text
    :return: the number of words
    Example: 
           print (get_word_number("this is a number 's ")) 
    '''
    return float(len(re.findall(r'\w+', text)))


# In[10]:

# get paragraph number
def get_para_number(text):
    '''
    Get the number of paragraphs.
    :param text: the raw text.
    :return: the number of paragraphs.
    Example: 
            s = "This is first. this is first. \n This is sencond. \n\n this is third." \
            print (get_para_number(s))
    '''
    paraList = text.splitlines()
    paraList[:] = [element for element in paraList if element != ""]
    return len(paraList)


# In[11]:

# get sent number 
def get_sent_number(text):
    '''
    Get the number of sentences in the text
    :param text: the raw text
    :return: the number of sentences 
    Example: 
            print (get_sent_number("This is number one. This ise number2, and number 2."))
    '''
    paraList = text.splitlines()
    paraList[:] = [element for element in paraList if element != ""]
    count = 0 
    for t in paraList:
        count = count + len(nltk.sent_tokenize(t))
    return float(count)


# In[12]:

# average sents number in paragraph 
def avg_sents_para(text):
    sents_num = get_sent_number(text)
    para_num = get_para_number(text)
    return round(float(sents_num)/para_num ,2 )


# In[13]:

# average word number in sents
def avg_word_sents(text):
    sents_num = get_sent_number(text)
    word_num = get_word_number(text)
    return round(float(word_num)/sents_num ,2 )


# In[18]:

from string import punctuation
from collections import Counter

def get_punc_sent(text):
    '''
    Get the number of punctuation number in the raw text
    :param text: the raw text
    :return: the number of words   
    '''
    counts = Counter(text)
    punctuation_counts = {k:v for k, v in counts.items() if k in punctuation}
    count = 0
    for k in punctuation_counts.keys():
        count = count + punctuation_counts[k]
    
    return count 
        
def get_punc_text(text):
    paraList = text.splitlines()
    paraList[:] = [element for element in paraList if element != ""]
    count = 0 
    for t in paraList:
        count = count + get_punc_sent(t)
    return count 


# In[19]:

# average punc number in sents 
def avg_puncts_sents(text):
    puncts_num = get_punc_text(text)
    sents_num = get_sent_number(text)
    return round(float(puncts_num)/sents_num ,2 )


# In[22]:

def features_summary(text):
    values =  [
        # text_grammar_check(text),
        get_spelling_error_number(text),
        get_word_number(text),
        get_para_number(text),
        get_sent_number(text),
        avg_sents_para(text),
        avg_word_sents(text),
        get_punc_text(text),
        avg_puncts_sents(text)
    ]
    return values


# In[23]:

# print (features_summary(X[0]))


# In[ ]:



