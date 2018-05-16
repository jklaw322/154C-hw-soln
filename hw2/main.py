import binarycodes
import numpy as np
import random
import matplotlib.pyplot as plt
from math import log2

#Question 1
#see matlab code

#Question 2

#part a
for k in range(2,11):
    num_phrases = 2**k
    pmf = [0.9,.1]
    output_q1 = binarycodes.tunstall(pmf, num_phrases)
    avg = k/np.array([len(s) for s in output_q1[0]]).dot(np.array(output_q1[1]))
    print("for num_phrases=%d length of codewords per average number of symbols = %f" %(num_phrases,avg))

#part b
x = []
y = []
for _ in range(100):
    num_phrases = 1024
    p = random.random()
    x.append(p)
    pmf = [p,(1-p)]
    output_q2 = binarycodes.tunstall(pmf, num_phrases)
    avg = log2(1024)/np.array([len(s) for s in output_q2[0]]).dot(np.array(output_q2[1]))
    y.append(avg)

plt.plot(np.array(x),np.array(y),"o")
plt.xlabel('p')
plt.ylabel('len codeword/avg # symbols')
plt.title('length of codewords per average number of symbols vs p (part b)')
plt.show()

#part c
x = []
y = []
for _ in range(100):
    num_phrases = 1024
    p = random.random()
    x.append(p)
    pmf = [p,(1-p)]
    tunstall_code = binarycodes.tunstall(pmf, num_phrases)

    #sort tunstall code
    pmf = {tunstall_code[0][i]: tunstall_code[1][i] for i in range(len(tunstall_code[0]))} # Uses dictionaries to implement huffman code
    pmf = sorted(pmf.items(),key=lambda x:x[1],reverse=True)
    pmf = dict(pmf)

    pmf_list = list(pmf.values())

    huffman_code = binarycodes.binaryHuffman(pmf)
    h_pmf = list(huffman_code.values())
    h_alphabet = list(huffman_code.keys())

    avg = log2(1024)/np.array([len(s) for s in h_alphabet]).dot(np.array(pmf_list))
    y.append(avg)

plt.plot(np.array(x),np.array(y),"o")
plt.xlabel('p')
plt.ylabel('len codeword/avg # symbols')
plt.title('length of codewords per average number of symbols vs p (part c)')
plt.show()
