# -*- coding: utf-8 -*-

# This script is used for getting the features of essays to build a machine learning model
'''
This script includes several functions, including:
    1. grammar error number check
    2. Spelling error number check 
    3. Number of sentence 
    4. Average length of sentences 
    5. Word Count
    6. Paragraph number 
'''

import re
from collections import Counter

import language_check

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


