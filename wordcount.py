

import sys 
from collections import Counter

for i in range(1,len(sys.argv)):

    filename= sys.argv[i]
    print("filename:", filename)


def count_word(filename):
    """Counts words in file and prints them.

    Arguments:
    -File 

    Return:
    -Dictionary containing word (key) and their counts (values)
    """

    file_containing_words = open(filename).read().replace("\n"," ").split(" ")
    print(file_containing_words)

    words_with_counts = {} #To store the count of each word

    special_chars = set(['.', ',', ':', '?', '"', '!']) #sets are faster than lists.

    cnt = Counter()

    #for line in file_containing_words: #Loop through each line, creating lists
            
    #    line = line.rstrip().split(" ")
            

    for word in file_containing_words: #Loop through each word in each list 

        word = word.lower()

        for char in word:
            if char in special_chars:
                word = word.replace(char,"")

        cnt[word] += 1

                #words_with_counts[word] = words_with_counts.get(word, 0) + 1   
    print("cnt", cnt)
    return cnt


def sort_alphabetically(word_counts):
    """Sort dictionary alphabetically by key."""

    [print(f"{key} {value}") for (key, value) in 
    sorted(word_counts.items(), key=lambda x: x[0])]
        
    return sorted(word_counts.items(), key=lambda x: x[0])


def sort_descending_values(word_counts):
    """Sort dictionary by descending order of values."""

    [print(f"{key} {value}") for (key, value) in 
    sorted(word_counts.items(), key=lambda x: x[1], reverse=True)]
        
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)


def sort_descending_values_and_alphabetically_by_keys(word_counts):
    """Sort dictionary first by descending order of values and then second by 
    alphabetical words"""

    [print(f"{key} {value}") for (key, value) in 
    sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))]
         
    return sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))


cnt_dict = count_word(filename)

sort_alphabetically(cnt_dict)

sort_descending_values(cnt_dict)

sort_descending_values_and_alphabetically_by_keys(cnt_dict)
