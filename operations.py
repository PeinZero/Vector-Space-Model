from vector_space import make_vector_space
from inverted_index import make_inverted_index
from nltk.stem import WordNetLemmatizer
import re
import os.path
import json

def searching(query_vector, inverted_index):
    size = len(query_vector)
    results = {}

    # Create Vector Space if not already created, otherwise get Vector Space from vector_space.json file.
    if not os.path.exists("vector_space.json"):
        vector_space = make_vector_space(inverted_index)

        json_object = json.dumps(vector_space, indent = 4) 
        with open("vector_space.json", "w") as outfile: 
            outfile.write(json_object)
    else:
        with open('vector_space.json') as json_file:
            vector_space = json.load(json_file)

    # Calculate Cosine Similarity between query and documents vector
    for vector in vector_space.keys():
        cosine_value = 0
        for term_tf_idf_value in range(size):
            cosine_value += vector_space[vector][term_tf_idf_value] * query_vector[term_tf_idf_value]
        results[vector] = cosine_value
    
    return dict(sorted(results.items(), key=lambda item: item[1],reverse=True))


def processing_query(query):
    
    lemmatizer = WordNetLemmatizer()
    # Create Inverted Index if not already created else get Inverted Index from inverted_index.json file.
    if not os.path.exists("inverted_index.json"):
        inverted_index = make_inverted_index()

        json_object = json.dumps(inverted_index, indent = 4) 
        with open("inverted_index.json", "w") as outfile: 
            outfile.write(json_object)

    else:
        with open('inverted_index.json') as json_file:
            inverted_index = json.load(json_file)

    # query processing
    query = re.sub("[^\w\s]|_", '', query).strip().lower().split(" ")
    query = [lemmatizer.lemmatize(term) for term in query]

    # creating query vector
    query_vector = []
    for term in inverted_index:
        if term in query:
            query_vector.append(1)
        else:
            query_vector.append(0)

    # return the ranked results
    return searching(query_vector,inverted_index)





