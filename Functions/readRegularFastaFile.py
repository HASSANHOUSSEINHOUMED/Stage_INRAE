from Bio import SeqIO
import numpy as np
import gzip

def readRegularFastaFile(fasta_file,max_length):
    # initialize our list to 4 taking into account the maximum size of the 
    # sequences between the two files
    listnumj = [[4]*max_length]
    seql_list=[]
     # unzip our zip file
    with gzip.open(fasta_file, "rt") as handle:
        for record in SeqIO.parse(handle, "fasta"):
             seqj=str(record.seq)
             # make all letters uppercase
             seqj=seqj.upper() 
             # replace all letters with integers in strings
             seqj=seqj.replace("A", "0")
             seqj=seqj.replace("C", "1")
             seqj=seqj.replace("G", "2")
             seqj=seqj.replace("T", "3")
             seqj=seqj.replace("U", "3")
             seqj=seqj.replace("R", "4")
             seqj=seqj.replace("Y", "4")
             seqj=seqj.replace("M", "4")
             seqj=seqj.replace("K", "4")
             seqj=seqj.replace("S", "4")
             seqj=seqj.replace("W", "4")
             seqj=seqj.replace("H", "4")
             seqj=seqj.replace("B", "4")
             seqj=seqj.replace("V", "4")
             seqj=seqj.replace("D", "4")
             seqj=seqj.replace("N", "4")
             # render everything to integers without looping using map function
             mapnumj=map(int,list(seqj))
             # make list
             listnumj_2=list(mapnumj)
             seql_list.append(listnumj_2)
                
    while (len(listnumj) < len(seql_list)):
        listnumj.append([4]*max_length)
     
    for i in range(len(seql_list)):
        for j in range(len(seql_list[i])):
            listnumj[i][j]=seql_list[i][j]
      

    X_array=np.array(listnumj).astype(np.int8)
    
    return X_array   
