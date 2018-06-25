import pickle
import numpy as np

if __name__ == '__main__':
    #find vocabulary_size = 8000
    with open(r"ctrsr_datasets/citeulike-t/vocabulary.dat" , encoding = 'utf-8') as vocabulary_file:
        vocabulary_size = len(vocabulary_file.readlines())

    #find item_size = 16980
    with open(r"ctrsr_datasets/citeulike-t/mult.dat" , encoding = 'utf-8') as item_info_file:
        item_size = len(item_info_file.readlines())

    #initialize item_infomation_matrix (16980 , 8000)
    item_infomation_matrix = np.zeros((item_size , vocabulary_size))

    #build item_infomation_matrix
    with open(r"ctrsr_datasets/citeulike-t/mult.dat" , encoding = 'utf-8') as item_info_file:
        sentences = item_info_file.readlines()

        for index,sentence in enumerate(sentences):
            words = sentence.strip().split(" ")[1:]
            for word in words:
                vocabulary_index , number = word.split(":")
                item_infomation_matrix[index][int(vocabulary_index)] =number

    ##############################################################################################            

    #find user_size = 5551
    with open(r"ctrsr_datasets/citeulike-t/users.dat" , encoding = 'utf-8') as rating_file:
        user_size = len(rating_file.readlines())

    #initialize rating_matrix (5551 , 16980)
    import numpy as np
    rating_matrix = np.zeros((user_size , item_size))

    #build rating_matrix
    with open(r"ctrsr_datasets/citeulike-t/users.dat" , encoding = 'utf-8') as rating_file:
        lines = rating_file.readlines()
        for index,line in enumerate(lines):
            items = line.strip().split(" ")
            for item in items:  
                rating_matrix[index][int(item)] = 1

    ##############################################################################################                        

    with open(r'item_infomation_matrix_t.pickle', 'wb') as handle:
        pickle.dump(item_infomation_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open(r'rating_matrix_t.pickle', 'wb') as handle:
        pickle.dump(rating_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
        
    #find vocabulary_size = 8000
    with open(r"ctrsr_datasets/citeulike-a/vocabulary.dat") as vocabulary_file:
        vocabulary_size = len(vocabulary_file.readlines())

    #find item_size = 16980
    with open(r"ctrsr_datasets/citeulike-a/mult.dat") as item_info_file:
        item_size = len(item_info_file.readlines())

    #initialize item_infomation_matrix (16980 , 8000)
    item_infomation_matrix = np.zeros((item_size , vocabulary_size))

    #build item_infomation_matrix
    with open(r"ctrsr_datasets/citeulike-a/mult.dat") as item_info_file:
        sentences = item_info_file.readlines()

        for index,sentence in enumerate(sentences):
            words = sentence.strip().split(" ")[1:]
            for word in words:
                vocabulary_index , number = word.split(":")
                item_infomation_matrix[index][int(vocabulary_index)] =number

    ##############################################################################################            

    #find user_size = 5551
    with open(r"ctrsr_datasets/citeulike-a/users.dat") as rating_file:
        user_size = len(rating_file.readlines())

    #initialize rating_matrix (5551 , 16980)
    import numpy as np
    rating_matrix = np.zeros((user_size , item_size))

    #build rating_matrix
    with open(r"ctrsr_datasets/citeulike-a/users.dat") as rating_file:
        lines = rating_file.readlines()
        for index,line in enumerate(lines):
            items = line.strip().split(" ")
            for item in items:  
                rating_matrix[index][int(item)] = 1

    ##############################################################################################                        

    with open(r'item_infomation_matrix_a.pickle', 'wb') as handle:
        pickle.dump(item_infomation_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open(r'rating_matrix_a.pickle', 'wb') as handle:
        pickle.dump(rating_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)


