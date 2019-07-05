#!/usr/bin/env python3
import sys

from bst import *

def main():

#--------------------------------------------------
#Add bad Words to the binary tree
    in_file = open("badWords.txt", "r")
    file_Read = in_file.readline()

    TreeSetVal = TreeSet()

    while file_Read != "":
        TreeSetVal.insert(file_Read.strip())
        file_Read = in_file.readline()
    in_file.close()

#--------------------------------------------------

    book_hd = open(sys.argv[1],'r')
    matchCount = 0
    for line in book_hd:
        for book_Word in line.split():
            Word=book_Word.strip()
            if Word.isalpha():
                if Word.lower() in TreeSetVal:
                    print(Word)
                    matchCount +=1
                else:
                    continue
            else:
                continue
                
    print("Count: ",matchCount)
main()
