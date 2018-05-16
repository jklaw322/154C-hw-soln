import string

def tunstall(pmf,num_phrases):

    #create an alphabet corresponding to the pmf
    alphabet = []
    for letter in string.ascii_uppercase:
        while(len(alphabet)<len(pmf)):
            alphabet.append(letter)
            break

    #initialize the tunstall code as a list of tuples
    code = [(a,pmf[i]) for i, a in enumerate(alphabet)]

    secondele = lambda x:x[1]
    while(len(code)<num_phrases):

        #find tuple with maximum probability and store in max_a,max_prob
        max_a, max_prob = max(code, key=secondele)

        max_i = [index for index,(i,j) in enumerate(code) if (i,j) == (max_a, max_prob)]

        #create next leaf
        new_leaf = [(max_a + s, max_prob * pmf[i]) for i,s in enumerate(alphabet)]
        code = code.__add__(new_leaf)

        avg_len_source = avg_len_source + code[max_i[0]]

        del code[max_i[0]] #delete maximum index
        #note:break ties by taking the first maximum probability on the LHS

    avg_length = num_phrases/avg_len_source

    return code,avg_length
