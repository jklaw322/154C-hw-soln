import re

def MatchLengthPosition(window,text):
    #base case is when window is '' and second elif is checking if any part of window is in text
    if(window==''):
        return [0,text[0]]
    elif(not any(re.search(window[i],text[0]) for i in range(len(window)))):
        return [0,text[0]]

    #Find the first match of sliding window in that string. Then return that string.
    m = False
    len_window = len(window)
    len_text = len(text)
    for i in range(len_window):
        if(m):
            print(source_letter)
            break
        else:
            for j in range(len_text):
                if(window[i:j]):
                    m = re.match(window[i:j],text)
                    match = bool(m)
                    if(match):
                        source_letter = m.group(0)
    return [1,len(window)-window.rindex(source_letter) - 1,len(source_letter)]
