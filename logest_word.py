def longest_word(sentence: str) -> str:

    split_text = sentence.split()
    letter_counter = ()

    for i in split_text:
        letter_counter += (len(i),)

    bigger = 0

    for i in letter_counter: 

        if i > bigger:

            bigger = i
            word_index = letter_counter.index(i)

    return split_text[word_index]


def longest_word2(sentence: str) -> str:

    bigger = 0
    word_index = None

    for i in sentence.split():

        if len(i) > bigger:

            bigger = len(i) 
            word_index = sentence.split().index(i)

    return sentence.split()[word_index]


def longest_word3(sentence: str) -> str:

    if sentence == "" or sentence == " ":

        return ""
    
    else:

        array = sentence.split()
        bigger_num = 0 
        word_index = 0

        for i in array:

            if len(i) > bigger_num:

                bigger_num = len(i)
                word_index = array.index(i)
        
        return array[word_index]


def longest_word4(sentence: str) -> str:
    
    return max(sentence.split(), key=len, default='')
