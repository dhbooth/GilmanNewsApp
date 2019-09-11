#!/usr/bin/python
def breaklines(string, character):
    temp=""
    index_of_space2=""
    while len(string)>character:
        for num in range(character, 0, -1):
            if string[num]==" ":
                index_of_space=num
                break
        for n in range(character+1, len(string)):
            if string[n]==" ":
                index_of_space2=n
                break
        if index_of_space2!="":
            if character-index_of_space<index_of_space2-character:
                actual_index_of_space=index_of_space
            else:
                actual_index_of_space=index_of_space2
        else:
            actual_index_of_space=index_of_space
        temp+= string[0:actual_index_of_space] + '\n'
        string= string[actual_index_of_space+1:len(string)]
        if len(string)<=character:
            temp+=string
    if temp!="":
        string=temp
    return string

