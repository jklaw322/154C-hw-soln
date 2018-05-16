import string
import itertools
from sys import setrecursionlimit

def inputlist(input_temp,input,n):#alter input for n source symbols
    if (n==1):
        return input
    else:
        n -= 1
        return inputlist(input_temp,[i*j for i in input_temp for j in input],n)

def binaryHuffman(pmf): #iterative
    key_list = []
    keyinsert = key_list.insert
    secondele = lambda x: x[1]
    while(len(pmf) > 2):
        #find key
        pmf_sort = sorted(pmf.items(),key=secondele) #sort by second element from every touple
        (key1, key2) = (pmf_sort[1][0],pmf_sort[0][0]) # get the key for the 2 smallest probabilities

        #store combined key
        pmf[f'{key1}{key2}'] = pmf[key1] + pmf[key2]
        keyinsert(0,(key1,key2))
        del pmf[key1]
        del pmf[key2]

    code = {alphabet:str(i) for (i,alphabet) in enumerate(pmf.keys())}

    for (key1,key2) in key_list:
        code[key1],code[key2] = code[f'{key1}{key2}'] + '0', code[f'{key1}{key2}'] + '1'
        del code[f'{key1}{key2}']

    return code

for n in range(8,9):
    input = [0.53, 0.28, 0.1, 0.05, 0.04]
    input = inputlist(input,input,n)
    input = sorted(input,reverse=True)
    # print('input (sorted) is: ', input)
    # print('Sum should be (approx): ', 1, 'Sum is: ', sum(input))
    # print('Length should be: ',2**n, 'Length is: ', len(input))
    # preprocess the pmf by making it an alphabetical dictionary.
    # Create a dict some arbitrary corresponding alphabet "letters" (just numbers from range
    pmf={('X'+str(alphabet)): input[i] for (i,alphabet) in enumerate(range(len(input)))}

    # Uses dictionaries to implement huffman code
    pmf_list = list(pmf.values())

    output = list(binaryHuffman(pmf).values())
#    print('Huffman Code =', output,'for n=',n)
    L = [len(output[i])*pmf_list[i] for i in range(len(pmf_list))]
    print('Average Length =', sum(L))
