import os
import pickle

def appendFiles(directory):
    cat_array = []
    for filename in os.listdir(directory):
        
        f = os.path.join(directory, filename)
        cat = load(f)
        cat_array.append(cat)

    return cat_array

def load(file_name):
    with open(file_name, 'rb') as file:
        var = pickle.load(file)
    return var