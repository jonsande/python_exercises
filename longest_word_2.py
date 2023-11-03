'''
Have the function LongestWord(sen) take the sen parameter being passed 
and return the longest word in the string. If there are two or more words 
that are the same length, return the first word from the string with that 
length. Ignore punctuation and assume sen will not be empty. Words may also 
contain numbers, for example "Hello world123 567"

Examples:

Input: "fun&!! time" Output: time

Input: "I love dogs" Output: love
'''


def longestword(sen: str) -> str:
    '''
    Find longest word in sentence
    '''

    sen = sen.split()
    
    word_cache = ""
    output = []
    
    for i in sen:
        for e in i:
            if e.isalnum():
                word_cache += e
            
        if len(word_cache) > 0:
            output.append(word_cache)
            word_cache = ""
        
    output.sort(reverse=True, key=len)
    
    return output[0]


# Otra solución
def longestword(sen: str) -> str:
    '''
    Find longest word in sentence
    '''

    sen = sen.split()
    
    word_cache = ""
    output = []
    
    for i in sen:
        for e in i:
            if e.isalnum():
                word_cache += e
            
        if len(word_cache) > 0:
            output.append(word_cache)
            word_cache = ""
    
    return max(output, key=len)


# Otra solución
import re
pattern = re.compile(r'\W+')
def LongestWord(sen): 
    x = pattern.split(sen)
    return max(x, key=len)


# Otra solución
import re

def LongestWord(sen): 
  
    sen = sen.strip()
    cleaned_sen = re.sub('[^A-Za-z]+', ',', sen)
    cleaned_sen_list = cleaned_sen.split(',')
    
    word = ''
    for i in cleaned_sen_list:
      if len(i) > len(word):
        word = i
      elif len(i) == len(word):
        pass
    
    return word