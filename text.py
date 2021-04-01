# -*- coding: utf-8 -*-

def revword(word:str) -> str:
    word = word.lower() 
    str = word[::-1]
    return str


def countword()->int:
    text= open('text.txt', 'r')
    count = 0
    i = 0
    for line in text :
        if i == 0:
            word =line.rstrip("\n")
            word = word.lower() 
            i = 1
            count = count + 1
        else:
            word1 = line.split()
            #print(sen)
            for i in word1:
                
                word1_new = revword(i)
                if word1_new == word:
                    count = count +1
    return count

print(countword())
