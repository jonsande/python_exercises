def anagram_checker(text: str, sub_text: str) -> bool:       
    """
    Check if a sentence is anagram of another
    """
    
    text = text.replace(" ", "")
    text = text.lower()
    sub_text = sub_text.replace(" ", "")
    sub_text = sub_text.lower()

    for i in text:
        if i not in "abcdefghijklmnñopqrstuvwxyz":
            text = text.replace(i, "")

    for i in sub_text:
        if i not in "abcdefghijklmnñopqrstuvwxyz":
            sub_text = sub_text.replace(i, "")
    
    dict_a = {}
    dict_b = {}

    for i in set(text):
        dict_a[i] = text.count(i)
    for i in set(sub_text):
        dict_b[i] = sub_text.count(i)

    if dict_a == dict_b:
        return True
    else:
        return False