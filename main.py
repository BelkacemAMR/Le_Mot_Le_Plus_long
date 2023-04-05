def longest_word(text):
    L = text.split()
    mot = ""
    for x in L:
        if(len(x)>len(mot)):
            mot = x
    return mot