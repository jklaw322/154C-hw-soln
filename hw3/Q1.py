import re
import numpy as np

def match_length(window,text):
    # if(len(window)<len(txt)):
    #     raise whatever error that it raises

    #convert txt to a list of words
    txt = text.split()
    win = window.split()

    txt = " ".join(sorted(set(txt), key=txt.index)) #remove repeats
    txt = txt.split()

    matches = [0] * len(txt)
    print(txt)
    print(matches)

    for i,word in enumerate(txt):
        n = 0
        words = list(txt)
        matches[i] = is_match(word,words,n)

    return matches


def is_match(win,words,match):
    if(win not in words):
        return 0

    for win in words:
        if(win in words):
            match = match + 1

    return match

def MatchLengthPosition(window, text):
    if(window not in text):
        return [0,text[0]]

    win = re.sub(' ', '', window) #window without spaces
    index = max(loc for loc, val in enumerate(text.split()) if val == win)

    win = str(window)
    txt = str(text)
    match = 0
    while(win in txt):
        index_match = text.rindex(win)
        txt = txt.replace(win,'',1)
        match += 1

    return [1,index+1,len(window)*match]

def MatchLengthPosition(window, text):
    if(window not in text):
        return [0,text[0]]

    #create copies of window,text
    win = str(window)
    txt = str(text)

    index = txt.rfind(win) #find index where window is
    txt_rm = (txt[:index] + txt[index+len(win):]).split() #remove that from string
    # find index where there is a discrepency
    for i,_ in enumerate(txt_rm):
        if txt.split()[i]!=txt_rm[i]:
            index = i
            break

#    byte_txt = bytearray(text.encode())
#    byte_txt[index:len(word)+index] = ' / '
#    print(byte_text.sort().index('/'))
    match = 0
    while(win in txt):
        index_match = text.rindex(win)
        txt = txt.replace(win,'',1)
        match += 1

    return [1,index+1,len(window)*match]
