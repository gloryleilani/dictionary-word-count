
def count_word(filename):
    """Counts words in file and prints them.

    Arguments:
    -File 

    Return:
    None

    
    """

    file_containing_words = open(filename)

    words_with_counts = {} #To store the count of each word

    for line in file_containing_words: #Loop through each line, creating lists
        
        
        line = line.rstrip().split(" ")
        
        for word in line: #Loop through each word in each list 

            words_with_counts[word] = words_with_counts.get(word, 0) + 1

    for key, value in words_with_counts.items():
        print(f"{key} {value}")

count_word("test.txt")
