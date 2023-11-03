def count_occurrences(main_str: str, sub_str: str) -> int:

    main_str = main_str.lower()
    sub_str = sub_str.lower()
    #counter = main_str.count(sub_str)
    #index_range = len(sub_str) - 1

    count = 0
    
    for i in range(len(main_str) - len(sub_str) + 1):
        if main_str[i:i+len(sub_str)] == sub_str:
            count += 1

    return count

print(count_occurrences("appleappleapple", "apple"))
