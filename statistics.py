# -*- coding: utf-8 -*-

# this is code for the statistics for a text, includes: words number, sentence number, paragragh number, sentnce length derivation
# we will add more features in this file.

import nltk
import math
import re

# get the number of words
def getWordCount(text):
	#split the text into words
	wordList = re.findall(r'\w+', text)
	return len(wordList)

# get the number of sentences
def getSentenceCount(text):
	#split the essay into sentences
	sentList = nltk.sent_tokenize(text)
	return len(sentList)


# get the number of paragrahs
def getParaCount(text):
	#split the text into paragraphs
	paraList = text.splitlines()
	#remove blank lines from the list of paragraphs
	paraList[:] = [element for element in paraList if element != ""]
	#print paraList
	return len(paraList)


# get the average length of sentences
def getAvgSentenceLength(text):
	#split the essay into sentences
	sentList = nltk.sent_tokenize(text)

	sumSentLength = 0
	for sent in sentList:
		sumSentLength = sumSentLength + getWordCount(sent)

	#print float(sumSentLength)/len(sentList)
	return float(sumSentLength)/len(sentList)


# get the derivation of sentence length
def getStdDevSentenceLength(text):
    # split the essay into sentences
    sentList = nltk.sent_tokenize(text)

    # mean sentence length
    mean = getAvgSentenceLength(text)

    nr = 0.0
    for sent in sentList:
        nr = nr + (getWordCount(sent) - mean) ** 2
    # print math.sqrt(nr/len(sentList))
    return math.sqrt(nr / len(sentList))


# test samples
# s = "This is a test. Second sentence. \n This is the third test. "
# print (getWordCount(s))
# print (getSentenceCount(s))
# print (getParaCount(s))
# print (getAvgSentenceLength(s))
# print (getStdDevSentenceLength(s))