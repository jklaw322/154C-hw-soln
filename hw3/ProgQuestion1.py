import re

def MatchLengthPosition(window,text):
    win = str(window)
    txt = str(text)

    if(win==''):
        return [0,text[0]]

    if(not any(re.search(win[i],txt[0]) for i in range(len(win)))):
        return [0,text[0]]

    #find sequence repeated at beginning of a string
    repeated,seq = _find_repeat(win,txt)

    matches = 0

    if((not repeated) and (not seq)):
        x = MatchLengthPosition1char(window,text)
        return x

    if(not seq):
        #now check for matches with txt
        while(re.match(repeated,text)):
            text = txt.replace(repeated,'',1)
            matches += 1
        if (len(win)>len(text)):
            return [1,len(repeated)-1,matches*len(repeated)]
        else:
            return [1,len(win)-1,matches*len(repeated)]

    if(_some_repeat(seq,win)): #if window is a sum of smallest repeatable sequences
        while(re.match(repeated,txt)):
            txt = txt.replace(repeated,'',1)
            matches += 1

        return [1,len(seq)-1,matches*len(win)]
    elif (repeated==win):
        return [1,len(win)-1,len(win)]

def _find_repeat(win,txt):
    seq = []
    if len(win)<=len(txt):
        for i in range(1,len(win)+1):
            seq_equal = (win[:i]==txt[:i])

            if(seq_equal== False):
                break

            seq = win[:i]
        if(seq):
            repeated = seq
            if(win==seq): #extra process step if window is exactly the repeated sequence
                seq=_process_win(win)
        else:
            repeated = None
            seq = None
    else:
        for i in range(1,len(txt)+1):
            seq_equal = (win[:i]==txt[:i])

            if(seq_equal== False):
                break
            seq = txt[:i]
        if(seq):
            repeated = seq
        else:
            repeated = None
            seq = None

    return repeated,seq

def _process_win(win):
    for i in range(1,len(win)):
        for j in range(0,len(win)):
            if win[:i]==win[j:j+len(win)]:
                return win[:i]

def _some_repeat(s1,win):
    for i in range(1,len(win)+1):
        if (s1*i==win):
            return True

    return False

def _MatchNoRepeats(win,text):
    index = []
    if(len(text)>len(win)):

        for i in range(len(text)):
            for j in range(len(text)):
                if(win[i:j]==text[i:j]):
                    index.append(i)
    else:
        for i in range(len(win)):
            for j in range(len(win)):
                if(win[i:j]==text[i:j]):
                    index.append(i)
    index = index[-1]

    txt = str(text)
    match = 0
    while(win in txt):
        index_match = text.rindex(win)
        txt = txt.replace(win,'',1)
        match += 1

    return [1,index+1,len(win)*match]
#
def MatchLengthPosition1char(window,text):
    index = []
    largest = max(len(text),len(window))
    smallest = min(len(text),len(window))
    for i in range(largest):
        for j in range(smallest):
            try:
                if(text[i+j]==window[j]):
                    win = window[j]
                    index = [largest - smallest - i]
                    break
            except:
                return [1,1,1] #hardcoded, what this value should be

        if(index):
            break

    match = 0
    txt = str(text)
    while(win in txt):
        index_match = text.rindex(win)
        txt = txt.replace(win,'')
        match += 1

    return [1,index[0],match]
                #found a match
def ParseSWLZ(win,input,size):
    index = 0
    win = ''
    for i in range(20):
        print(output)
        #1st iter
        cur_txt = input[index:]

        mlp = MatchLengthPosition(win,cur_txt)

        output.append(mlp)

        if(mlp[0]==1):
            len_match = mlp[2]
            index = index + len_match

            win = win + cur_txt[:len_match]
            if(len(win)>size): #trim window by taking out the overflow from size
                win = win[len(win)-size:]


        if(mlp[0]==0):
            index = index + 1

            if(len(win)<size):
                win = win + cur_txt[0]
            else:
                win = win[1:] + cur_txt[0]
