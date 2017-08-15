# -*- coding: utf-8 -*-

'''
Install Python package language-check first.https://pypi.python.org/pypi/language-check
This code only run under python3.
'''
import language_check

# input a sentence list
# return the number of grammar errors
def text_grammar_check(text):
    tool = language_check.LanguageTool('en-US')
    total_mistakes = 0
    for s in text:
        total_mistakes += sent_grammar_check(tool, s)
    return total_mistakes

def sent_grammar_check(tool, s):
    matches = tool.check(s)
    return len(matches)

# Examples
# text = u'A sentence with a error the the in the Hitchhiker’s Guide to the the Galaxy'
# print (text_grammar_check([text]))