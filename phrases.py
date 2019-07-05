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
    for item in wordList:
        wordList.append(item.strip().lower())

    # for Word in wordList:
    #     # fixedWord = Word.strip().lower()
    #     if Word in TreeSetVal:
    #         matchCount+=1
    #         print(Word)
    #     if wordList[wordList.index(Word)+1] in TreeSetVal:
    #         matchCount+=1
    #         print(Word + " " + wordList[wordList.index(Word)+1])
    #     if wordList[wordList.index(Word)+2] in TreeSetVal:
    #         matchCount+=1
    #         print(Word + " " + wordList[wordList.index(Word)+1] + " " + wordList[wordList.index(Word)+2])
    #     if wordList[wordList.index(Word)+3] in TreeSetVal:
    #         matchCount+=1
    #         print(Word + " " + wordList[wordList.index(Word)+1] + " " + wordList[wordList.index(Word)+2] + " " + wordList[wordList.index(Word)+3])
    #     if wordList[wordList.index(Word)+4] in TreeSetVal:
    #         matchCount+=1
    #         print(Word + " " + wordList[wordList.index(Word)+1] + " " + wordList[wordList.index(Word)+2] + " " + wordList[wordList.index(Word)+3]+ " " + wordList[wordList.index(Word)+4])
    #     else:
    #         continue
    # print("Count: ",matchCount)
    # # for line in book_hd:
    #     oldList =line.split()
    #     for item in oldList:
    #         lineList.append(item.lower())
    #     for book_list in line.split():
    #         Word=book_list.strip().lower()
    #         if Word in TreeSetVal:
    #             matchCount+=1
    #             print(Word)
    #             if lineList[lineList.index(Word)+1] in TreeSetVal:
    #                 matchCount+=1
    #                 print(Word + " " + lineList[lineList.index(Word)+1])
    #                 if lineList[lineList.index(Word)+2] in TreeSetVal:
    #                     matchCount+=1
    #                     print(Word + " " + lineList[lineList.index(Word)+1] + " " + lineList[lineList.index(Word)+2])
    #                     if lineList[lineList.index(Word)+3] in TreeSetVal:
    #                         matchCount+=1
    #                         print(Word + " " + lineList[lineList.index(Word)+1] + " " + lineList[lineList.index(Word)+2] + " " + lineList[lineList.index(Word)+3])
    #
    #                         if lineList[lineList.index(Word)+4] in TreeSetVal:
    #                             matchCount+=1
    #                         else:
    #                             continue
    #                     else:
    #                         continue
    #                 else:
    #                     continue
    #             else:
    #                 continue
    #         else:
    #             continue

    print("Count: ",matchCount)
main()
