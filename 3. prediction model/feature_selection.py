
# coding: utf-8

# # This script is used for getting the features of essays to build a machine learning model
# '''
# This script includes several functions, including:
#     1. grammar error number check
#     2. Spelling error number check 
#     3. Word Count
#     4. Number of sentence 
#     5. Average length of sentences 
#     6. Paragraph number 
# '''

# # Read data

# In[1]:

# import pandas as pd
# import numpy as np


# In[2]:

# read data 
# training_set = pd.read_csv("data/comments.csv", )


# In[3]:

# X = training_set['comment_text']
# y = training_set['commenter_credibility']


# In[4]:

# print (X[0])
# print (y[0])


# # Extract features

# In[5]:

import re
from collections import Counter
import nltk
import math
import re


# ## Grammar errors features
# Grammar errors are currently not considered due to the computation time and accuracy.

# ## Spelling 
# ### Some words that not appear in the en-spelling.txt are considered as errors. 

# In[6]:

# function 2: spelling error number checking. This function can be updated with nltk.
def get_words(text):
    ''' Get all the words in a text 
    :param text: raw text
    :return: all the words in the text
    Example: 
            print (get_words('I amd the .. . /3'))
    '''
    return re.findall(r'\w+', text.lower())

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

# print (get_spelling_error_number("he kk uu in jsas ssssss"))


# ## Wors Number 

# In[9]:

# Function 3: word count
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

# print (get_word_number("This is a . @@@  555 good point"))


# ## Sentence number 

# In[11]:

# Function 4: Number of sentence
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

# s = "This a first . and the Second! The "
# print (get_sent_number(s))


# In[13]:

## Get average sentence length


# In[14]:

# Function 5: Average length of sentences

def get_average_sent_length(text):
    '''
    Get the average sentence length of the given text.
    :param text: the raw text 
    :return: the average length of the sentences
    Example: 
            print (get_average_sent_length("this is. This is two. Three."))
    '''

    sents = nltk.sent_tokenize(text)
    num = get_sent_number(text)
    
    return round(get_word_number(text)/num,2)


# In[15]:

# s = "This ia first. ."
# print (get_sent_number(s))
# print (get_average_sent_length(s))


# # Get Paragraph number

# In[16]:

# Function 6: Paragraph number
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


# In[17]:

# i = 1
# print (X[i])
# print (get_para_number(X[i])) 


# ## Summary of features

# In[18]:

# summarize all the return value of the functions above.
def features_summary(text):
    '''
    Summary the function values of the functions above, so that don't need 
    to call funtions one by one. 
    :param text: the raw text 
    :return: a list contains all the information mentioned above.
    Examples:
            s = "This is a text. This is a text."
            print (inf_summary(s))
    '''
    values =  [
            # text_grammar_check(text),
            get_spelling_error_number(text),
            get_word_number(text),
            get_sent_number(text),
            get_average_sent_length(text),
            get_para_number(text)
        ]
    return values


# In[19]:

# i = 111
# print (X[i])
# print (y[i])
# print (features_summary(X[i]))

