#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for ch in str:
        if 'a' <= ch <= 'z':
            ch = chr(ord(ch[0]) - 32)
        newstr += ch
    return (newstr)
