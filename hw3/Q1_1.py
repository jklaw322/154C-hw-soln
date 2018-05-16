import re

def MatchLengthPosition(window,text):
    win = str(window)
    txt = str(text)

    if(txt[0] not in win):
        return [0,text[0]]

    starts_equal = re.match(win,txt[len(win):2*len(win)])

    if(starts_equal): # if starts are equal, there is a tie
        index = txt.rfind(win) - 1 #rightmost index
    else:
        index = len(win)-1 #index normally

    #find seq that is repeated in window and text

    for i in range(1,len(win)+1):
        seq_equal = (win[:i]==txt[:i])

        if(seq_equal== False):
            break

        seq = win[:i]

    #remove that sequence
    txt_rm = txt.replace(seq,'',1)

    #now find index

    matches = 0
    while(re.match(seq,txt)):#while there is a match
        txt = txt.replace(seq,'',1)
        matches += 1

    #find number of matches for that seq


    return [1,index,matches*len(seq)]
