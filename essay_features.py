# -*- coding: utf-8 -*-

# This script is used for getting the features of essays to build a machine learning model
'''
This script includes several functions, including:
    1. grammar error number check
    2. Spelling error number check 
    3. Word Count
    4. Number of sentence 
    5. Average length of sentences 
    6. Paragraph number 
'''

import re
from collections import Counter
import language_check
import nltk
import math
import re

# function 1: grammar error number checking
def text_grammar_check(text):
    '''
    :param text: sentence list, the original text has been separated into sentence lists
    :return: number of grammar errors
    Examples:
    text = u'A sentence with a error the the in the Hitchhiker’s Guide to the the Galaxy'
    print (text_grammar_check([text]))
    '''
    tool = language_check.LanguageTool('en-US')
    total_mistakes = 0
    for s in text:
        total_mistakes += sent_grammar_check(tool, s)
    return total_mistakes

def sent_grammar_check(tool, s):
    '''
    :param tool: tool is a language_ckeck function generated will the package language_ckeck model
    :param s: the string need to check
    :return: the number of grammar errors in this sentence 
    '''
    matches = tool.check(s)
    return len(matches)


# function 2: spelling error number checking. This function may be updated will nltk.
def get_words(text):
    ''' Get all the words in a text 
    :param text: raw text
    :return: all the words in the text
    Example: 
            print (get_words('I amd the .. . /3'))
    '''
    return re.findall(r'\w+', text.lower())

# Get all the words in en-spelling.txt which contains most words in English dictionary
WORDS = Counter(get_words(open('en-spelling.txt').read()))

def get_spelling_error_number(text):
    '''
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
            error_numer += 1
    return error_numer

# Function 3: word count
def get_word_number(text):
    '''
    Get the number of words in the raw text 
    :param text: the raw text
    :return: the number of words
    Example: 
           print (get_word_number("this is a number 's ")) 
    '''
    return len(re.findall(r'\w+', text))

# Function 4: Number of sentence
def get_sent_num(text):
    '''
    Get the number of sentences in the text
    :param text: the raw text
    :return: the number of sentences 
    Example: 
            print (get_sent_num("This is number one. This ise number2, and number 2."))
    '''
    return len(nltk.sent_tokenize(text))

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
    return get_word_number(text)/len(sents)

