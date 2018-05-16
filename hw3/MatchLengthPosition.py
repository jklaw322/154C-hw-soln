import re

def MatchLengthPosition2(window,text):
    for i in range(max(len(text),len(window))):
        for j in range(min(len(text),len(window))):
            if(text[i+j]==window[j]):
                index = len(text) - i

    return [1,index,matches]
                #found a match
