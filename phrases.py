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
    matchCount = 0
    wordList = []
    book_hd = open(sys.argv[1],'r')
    book_read = book_hd.read()
    BookList = book_read.split()
    wordCount = 0
    for item in BookList:
        if item.isalpha():
            wordList.append(item.strip().lower())
    for word in wordList:
        if word in TreeSetVal:
            print(word)
            matchCount+=1
        if (word+" "+wordList[wordCount+1]) in TreeSetVal:
            print(word+" "+wordList[wordCount+1])
            matchCount += 1
        if (word +" "+wordList[wordCount+1]+" "+wordList[wordCount+2]) in TreeSetVal:
            print(word +" "+ wordList[wordCount+1]+" "+wordList[wordCount+2])
            matchCount += 1
        if (word +" "+ wordList[wordCount+1]+" "+wordList[wordCount+2]+" " +wordList[wordCount+3]) in TreeSetVal:
            print(word +" "+ wordList[wordCount+1]+" "+wordList[wordCount+2] +" "+wordList[wordCount+3])
            matchCount += 1
        if (word +" "+ wordList[wordCount+1]+" "+wordList[wordCount+2]+" " +wordList[wordCount+3]+" "+wordList[wordCount+4]) in TreeSetVal:
            print(word +" "+ wordList[wordCount+1]+" "+wordList[wordCount+2]+" " +wordList[wordCount+3]+" "+wordList[wordCount+4])
            matchCount += 1
        else:
            wordCount+=1
            if ((wordCount+5)>len(wordList)):
                break
            continue
        wordCount+=1
    #
    print("Count: ",matchCount)
main()

