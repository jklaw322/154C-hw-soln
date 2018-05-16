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
