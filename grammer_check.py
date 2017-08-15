# -*- coding: utf-8 -*-

'''
Install Python package language-check first.
This code only run under python3.
https://pypi.python.org/pypi/language-check
This code is too slow.
'''
import language_check
tool = language_check.LanguageTool('en-US')
text = u'A sentence with a error the the in the Hitchhiker’s Guide to the the Galaxy'
matches = tool.check(text)
# print(matches[1])

# output all the grammer errors
# for item in matches:
#     print (item)

# print out the number of grammer errors.
print(len(matches))