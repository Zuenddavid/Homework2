from urllib.request import urlopen

url = "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"
local_name = "The_Great_Gatsby.txt"


def save_locally():
    """
    Save the book locally, so we can use it faster and no need to load every time
    :return: None
   """
    with open(local_name, "w") as local_fp:
        with urlopen(url) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)

save_locally()
punctuation = ",;!.?-()"
def get_unique_words():
    """
    Get the dictionary of unique words and their frequency
    :return: dict
    """
    unique_words = {}
    word_count = 0
    with open(local_name) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # get the words:
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1
                word_count += 1
    return unique_words, word_count

unique_words, word_count = get_unique_words()

def get_7_charachters():

    unique_words7 = []
    for word in unique_words.keys():
        if len(word) >= 7:
            unique_words7.append(word)
    return unique_words7

unique_words7 = get_7_charachters()

unique_words7 = len(unique_words7)
unique_word_1 = len(unique_words.keys())
unique_ratio = unique_word_1/word_count

from urllib.request import urlopen

url2="https://www.gutenberg.org/cache/epub/67627/pg67627.txt"
local_name2 = "The_Treasure_Trail.txt"
def save_locally2():
    """
    Save the book locally, so we can use it faster and no need to load every time
    :return: None
    """
    with open(local_name2, "w") as local_fp2:
        with urlopen(url2) as fp2:
            for line2 in fp2:
                line2 = line2.decode('utf-8-sig').replace("\n", "")
                local_fp2.write(line2)

save_locally2()

punctuation = ",;!.?-()"
def get_unique_words2():
    """
    Get the dictionary of unique words and their frequency
    :return: dict
    """
    unique_words2 = {}
    word_count2 = 0
    with open(local_name2) as fp:
        for line2 in fp:
            # remove punctuation
            for d in punctuation:
                line2 = line2.replace(d, " ")
            line2 = line2.lower()
            # get the words:
            for word2 in line2.split():
                unique_words2[word2] = unique_words2.get(word2, 0) + 1
                word_count2 += 1
    return unique_words2, word_count2

unique_words2, word_count2 = get_unique_words2()

def get_7_charachters2():

    unique_words7_2 = []
    for word2 in unique_words2.keys():
        if len(word2) >= 7:
            unique_words7_2.append(word2)

    return unique_words7_2

unique_words7_2 = get_7_charachters2()


unique_words7_2 = len(unique_words7_2)
unique_word_2 = len(unique_words2.keys())
unique_ratio_2 = unique_word_2/word_count2

rank = []
if unique_word_1 > unique_word_2:
    rank.append("more")
else:
    rank.append("less")

rank2 = []
if unique_words7 > unique_words7_2:
    rank2.append('more')
else:
    rank2.append('less')

print(f" Author of Book 1 has a vocabulary of {unique_word_1} words, whereas author of book 2 has a vocabulary of {unique_word_2} words\n"
      f" Therefore, the Author of Book 1 has {rank} vocabulary than author of book 2\n"
      f" Book 1 has {unique_words7} unique words with more than 7 characters whereas book 2 has {unique_words7_2}\n"
      f" Therefore, Book 1 has {rank2} unique words than book 2\n"
      f" The ratio between distinct words and total number of words in book 1 is {round(unique_ratio,4)} whereas {round(unique_ratio_2,4)} in book 2.")