import os
import re
from collections import OrderedDict
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
CURRENT_DIR = os.getcwd()

def make_inverted_index():
    inverted_index = {}

    # making Stop Word lists
    file_name = CURRENT_DIR + "\Stopword-List.txt"
    f = open(file_name, "r", encoding='UTF8')
    stop_words_list = f.read()
    stop_words_list = ' '.join(stop_words_list.split()).split(' ')
    stop_words_list.append(' ')
    f.close()

    for document_id in range(1, 51):
        count = 0

        # Opening and Reading the short stories
        file_name = CURRENT_DIR + '\ShortStories\\' + str(document_id) + '.txt'
        f = open(file_name, "r", encoding='UTF8')
        file_lines = f.readlines()

        for line in file_lines:

            # Removes all the punctuations and _ from the line, and whiteSpaces, \n and \t from each end of the line.
            line = re.sub("[^\w\s]|_", '', line).strip()

            # (' '.join(line.split())).split(' ') remove multi whiteSpace with a single whiteSpace
            for word in (' '.join(line.split())).split(' '):

                # To keep track of positions of term within each document.
                count = count + 1
                
                if word in stop_words_list:
                    continue

                # Case Foding
                word = word.lower()

                # Lemmatizing the word
                word = lemmatizer.lemmatize(word)

                # the making of inverted index
                if word in inverted_index:
                    if str(document_id) in inverted_index[word]:
                        inverted_index[word][str(document_id)].append(count)
                    else:
                        inverted_index[word][str(document_id)] = [count]
                    # endif
                else:
                    inverted_index[word] = {str(document_id): [count]}
                # endif
            # endfor
        # endfor
        f.close()
    # endfor
    return OrderedDict(sorted(inverted_index.items()))


    