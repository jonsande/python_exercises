'''
Using the Python language, have the function KUniqueCharacters(str) take 
the str parameter being passed and find the longest substring that contains 
k unique characters, where k will be the first character from the string. 
The substring will start from the second position in the string because the 
first character will be the integer k. For example: if str is "2aabbacbaa" 
there are several substrings that all contain 2 unique characters, namely: 
["aabba", "ac", "cb", "ba"], but your program should return "aabba" because 
it is the longest substring. If there are multiple longest substrings, then 
return the first substring encountered with the longest length. k will range 
from 1 to 6.

Input:"3aabacbebebe" Output:"cbebebe"

Input:"2aabbcbbbadef" Output:"bbcbbb"
'''


def kunique_characters(string: str) -> str:
    '''
    [Function doc]
    '''

    k = int(string[0])
    string = string[1:]
    matches = []
    end_i = len(string)
    
    while end_i >= k:
        
        for i in range(0, end_i):
            
            word = string[i:end_i]
            
            if len(set(word)) == k:
                matches.append(word)
        
        end_i -= 1
    
    matches.sort(reverse=True, key=len)

    return  matches[0]

kunique_characters("3aabacbebebe")
kunique_characters("2aabbcbbbadef")