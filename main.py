from urllib.request import urlopen

url = "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"
local_name = "The_Great_Gatsby.txt"


def save_locally(local_name,url):
    """
    Save the book locally, so we can use it faster and no need to load every time
    :return: None
   """
    with open(local_name, "w") as local_fp:
        with urlopen(url) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)

save_locally("Alice’s Adventures in Wonderland","https://www.gutenberg.org/files/11/11-0.txt")
save_locally("A Tale of Two Cities","https://www.gutenberg.org/files/98/98-0.txt")

punctuation = ",;!.?-()"
def get_unique_words(local_name):

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
    return unique_words,word_count

unique_words, word_count = get_unique_words(local_name)

def get_7_charachters(local_nam):

    unique_words7 = []
    for word in unique_words.keys():
        if len(word) >= 7:
            unique_words7.append(word)
    return unique_words7

unique_words7 = get_7_charachters(local_name)

def get_rank(B1,B2):
    rank = []
    if B1 > B2:
        rank.append("more")
    else:
        rank.append("less")
    return rank


UniquewordsB1, wordcountB1 = get_unique_words("The_Great_Gatsby.txt")
More_7 = get_7_charachters("The_Great_Gatsby.txt")
More_7B1 = len(More_7)
lenuniquewordsB1 = len(UniquewordsB1.keys())
unique_ratioB1 =lenuniquewordsB1/wordcountB1
print(lenuniquewordsB1, wordcountB1, unique_ratioB1)

UniquewordsB2, wordcountB2 = get_unique_words("A Tale of Two Cities")
More_72 = get_7_charachters("A Tale of Two Cities")
More_7B2 = len(More_72)
lenunqiuewordsB2 = len(UniquewordsB2.keys())
unique_ratioB2 =  lenunqiuewordsB2/ wordcountB2
print(lenunqiuewordsB2, wordcountB2, unique_ratioB2)

print(f" Author of Book 1 has a vocabulary of {lenuniquewordsB1} words, whereas author of book 2 has a vocabulary of {lenunqiuewordsB2} words\n"
      f" Therefore, the Author of Book 1 has {get_rank(lenuniquewordsB1,lenunqiuewordsB2)} vocabulary than author of book 2\n"
      f" Book 1 has {More_7B1} unique words with more than 7 characters whereas book 2 has {More_7B2}\n"
      f" Therefore, Book 1 has {get_rank(More_7B1,More_7B2)} unique words than book 2\n"
      f" The ratio between distinct words and total number of words in book 1 is {round(unique_ratioB1,4)} whereas {round(unique_ratioB2,4)} in book 2.")
