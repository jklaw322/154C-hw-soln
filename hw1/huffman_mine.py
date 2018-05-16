import string
import itertools

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

    counter = len(pmf) - 2 #count the length of pmf instead of checking len(pmf) > 2 every time
    while(counter>0):
        #find key
        pmf_sort = pmf.items()
        pmf_sort = sorted(pmf_sort,key=secondele) #sort by second element from every touple
        (key1, key2) = (pmf_sort[1][0],pmf_sort[0][0]) # get the key for the 2 smallest probabilities

        #store combined key
        pmf[f'{key1}{key2}'] = pmf[key1] + pmf[key2] #let pmf[key1+key2] be the sum of the smallest probabilities
        keyinsert(0,(key1,key2)) #insert (key1,key2) in beginning of list (0th entry)
        del pmf[key1] #delete the 2 smallest probablities so that can sort accordingly
        del pmf[key2]
        counter -= 1

    #initialize the output as a with a 0 on the top and 1 at the bottom (used the indicies to do this)
    code = {alphabet:str(i) for (i,alphabet) in enumerate(pmf.keys())}

    for (key1,key2) in key_list:
        code[key1],code[key2] = code[f'{key1}{key2}'] + '0', code[f'{key1}{key2}'] + '1'
        del code[f'{key1}{key2}']

    return code

for n in range(8,11):
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
    print('First 10 Huffman Codes =',output[0:10],'Average Length =', sum(L),'for n =',n)
