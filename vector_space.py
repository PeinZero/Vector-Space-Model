from inverted_index import make_inverted_index
import math

def make_vector_space(inverted_index):
    
    vector_space = {}
    
    # Creating document vectors
    for document_id in range(1, 51):
        vector_name = str(document_id)
        vector_space[vector_name] = []
        for term in inverted_index.keys():
            if str(document_id) in inverted_index[term].keys():
                # Calculating tf-idf
                tf = (1 + math.log( len( inverted_index[term][str(document_id)] ) ))
                idf = math.log( 50 / len(inverted_index[term].keys()) )
                
                vector_space[vector_name].append(tf * idf)
            else:
                vector_space[vector_name].append(0)
    
    #NORMALIZATION
    for vector in vector_space.keys():
        magnitude = 0

        #Calculating each vector magnitude
        for tf_idf_value in vector_space[vector]:
            magnitude += tf_idf_value*tf_idf_value
        magnitude = math.sqrt(magnitude)
        
        # Converting vectors to UNIT vectors
        vector_space[vector] = [(tf_idf_value/magnitude) for tf_idf_value in vector_space[vector]]


    return vector_space
