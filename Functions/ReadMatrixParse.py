import numpy as np
import os 
import pandas as pd
from scipy.sparse import coo_matrix

def ReadMatrixParse(your_folder_path,max_length):
    
    # list of files
    list_of_files=os.listdir(your_folder_path)
    
    # list of path to our files 
    path_of_matrix=[]

    for your_file_name in list_of_files:
        if 'dp.ps' in your_file_name:
            path_of_matrix.append(your_folder_path + '/' + your_file_name)

        
    listes=[]
    maxIndex=[]
 

    for i in range(len(path_of_matrix)):
        
    
        with open(path_of_matrix[i],'r') as f:
            lines = f.readlines()
         
    
        modified = []

        for line in lines:
            modified.append(line.strip())
            
        index_debut = modified.index('%start of base pair probability data')
        index_fin = modified.index('showpage')
    
        list1 = modified[index_debut+1:index_fin]

        p = []

        for k in range(len(list1)):
            l=list1[k].split()
            p.append(l)
    
        p=np.array(p)
        p=p[p[:,3]=="ubox"]

        p=p[:,0:3]
        p=p.astype("float")
    
        dat2 = pd.DataFrame(p)
    
        dat2.columns=['i','j','x']
    
        row  = dat2["i"].astype("int")-1

        col  = dat2["j"].astype("int")-1

        data = dat2["x"]
    
        maxIndex.append(max(col))

        matrix_parse = coo_matrix((data, (row, col)), shape=(max_length,max_length))
    
        listes.append(matrix_parse.toarray())
    
    return(listes,maxIndex)
