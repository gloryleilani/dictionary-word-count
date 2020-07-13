

import sys 

def count_word():
    """Counts words in file and prints them.

    Arguments:
    -File 

    Return:
    None


    """

    for i in range(len(sys.argv)):

        filename= sys.argv[i]

        file_containing_words = open(filename)

        words_with_counts = {} #To store the count of each word

        special_chars = ['.', ',', ':', '?', '"']

        for line in file_containing_words: #Loop through each line, creating lists
            
            line = line.rstrip().split(" ")
            
            for word in line: #Loop through each word in each list 

                word = word.lower()

                for char in word:
                    if char in special_chars:
                        word = word.replace(char,"")

                words_with_counts[word] = words_with_counts.get(word, 0) + 1

        for key, value in words_with_counts.items():
            print(f"{key} {value}")

count_word()
