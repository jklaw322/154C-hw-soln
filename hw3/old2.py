import re

def MatchLengthPosition(window, text):
    '''finds index where there is the longest match and len(window)*num matches'''
    if(window not in text):
        return [0,text[0]]

    #create copies of window,text
    win = str(window)
    txt = str(text)

    #finding the index where there is the longest match
    index = txt.rfind(win) #find index where window is
    # txt_rm = (txt[:index] + txt[index+len(win):]).split() #remove that from string
    # # find index where there is a discrepency
    # for i,_ in enumerate(txt_rm):
    # #find index (in list of words) where the string is removed by checking against original
    #     if txt.split()[i]!=txt_rm[i]:
    #         index = i
    #         break

    match = 0
    while(win in txt):
        index_match = text.rindex(win)
        txt = txt.replace(win,'',1)
        match += 1

    return [1,len(txt) - index,len(window)*match]
#
# def ParseSWLZ(input_txt,win_size):
#     i = 0
#     window = []
#     j = 0
#
#     while(length_done < length(input_txt)):
#         j = j  + 1
#         window.append(input_txt(i:len(input_text)))
#         MatchLengthPosition()
