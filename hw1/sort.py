#make sure sort works
pmf = { 'a': .35, 'b': 0.22, 'c': 0.15,'d':.09,'e':.09,'f':.05,'g':.05 }
pmf_sort = sorted(pmf.items(),key=lambda x: x[1],reverse=True) #sort by second element from every touple

print({alphabet:str(i) for (i,alphabet) in enumerate(pmf.keys())})
Input = [.3,.25,.2,.15,.1]

print({str(alphabet): Input[i] for (i,alphabet) in enumerate(range(len(Input)))})
print(pmf_temp)
