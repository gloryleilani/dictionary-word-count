

import sys 
from collections import Counter
from operator import itemgetter

for i in range(1,len(sys.argv)):

    filename= sys.argv[i]


def count_word(filename):
    """Counts words in file and prints them.

    Arguments:
    -File 

    Return:
    -Dictionary containing word (key) and their counts (values)
    """


    file_containing_words = open(filename)

    words_with_counts = {} #To store the count of each word

    special_chars = set(['.', ',', ':', '?', '"']) #sets are faster than lists.

    cnt = Counter()

    for line in file_containing_words: #Loop through each line, creating lists
            
        line = line.rstrip().split(" ")
            

        for word in line: #Loop through each word in each list 

            word = word.lower()

            for char in word:
                if char in special_chars:
                    word = word.replace(char,"")

            cnt[word] += 1

                #words_with_counts[word] = words_with_counts.get(word, 0) + 1
              
    return cnt


def sort_alphabetically(dict):
    """Sort dictionary alphabetically by key."""
    
    sorted_alpha_words_with_counts = sorted(dict.items(), key=lambda x: x[0])
         
    for key, value in sorted_alpha_words_with_counts:
        print(f"{key} {value}")

    return sorted_alpha_words_with_counts


def sort_descending_values(dict):
    """Sort dictionary by descending order of values."""

    sorted_descending_values_with_words = sorted(dict.items(), key=lambda x: x[1], reverse=True)
         
    for key, value in sorted_descending_values_with_words:
        print(f"{key} {value}")

    return sorted_descending_values_with_words


def sort_descending_values_and_alphabetically_by_keys(dict):
    """Sort dictionary first by descending order of values and then second by 
    alphabetical words"""

    sorted_two_attributes = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
    
    for key, value in sorted_two_attributes:
        print(f"sort_by descending_values_and_alphabetically_by_keys: {key} {value}")

    return sorted_two_attributes


dict = count_word(filename)

sort_alphabetically(dict)

sort_descending_values(dict)

sort_descending_values_and_alphabetically_by_keys(dict)
