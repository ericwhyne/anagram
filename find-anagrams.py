#!/usr/bin/python
import fileinput
import re
from collections import Counter

for line in fileinput.input():
  words = line[:-1].split(' ')
  anagrams = dict()
  print line[:-1]
  for word in words:
    word = word.lower()
    word = re.sub('[^a-zA-Z]','',word) # remove non alpha chars
    for other_word in words:
        other_word = other_word.lower()
        other_word = re.sub('[^a-zA-Z]','',other_word)
        anagram = True
        for char in word:
            if char not in other_word:
                anagram = False
        if word == other_word:
            anagram = False
        if anagram == True:
            print '\t' + word + '\t' + other_word
