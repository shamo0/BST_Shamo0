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
    for i in range(1,len(sys.argv)):
        try:
            wordList = []
            matchCount = 0
            book_hd = open(sys.argv[i],'r')
            book_read = book_hd.read()
            BookList = book_read.split()
            wordCount = 0
            for item in BookList:
                if item.isalpha():
                    wordList.append(item.strip().lower())
            for word in wordList:
                if word in TreeSetVal:
                    matchCount+=1
                if (word+" "+wordList[wordCount+1]) in TreeSetVal:
                    matchCount += 1
                if (word +" "+wordList[wordCount+1]+" "+wordList[wordCount+2]) in TreeSetVal:
                    matchCount += 1
                if (word +" "+ wordList[wordCount+1]+" "+wordList[wordCount+2]+" " +wordList[wordCount+3]) in TreeSetVal:
                    matchCount += 1
                if (word +" "+ wordList[wordCount+1]+" "+wordList[wordCount+2]+" " +wordList[wordCount+3]+" "+wordList[wordCount+4]) in TreeSetVal:
                    matchCount += 1
                else:
                    wordCount+=1
                    if ((wordCount+5)>len(wordList)):
                        break
                    continue
                wordCount+=1
            #
            print(str(sys.argv[i]),"count: ",matchCount)
        except:
            print("Enter files to process")
main()
